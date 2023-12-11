#!/usr/bin/env python3
"""
Improved personal stats parser. Give it a saved copy of your
   https://adventofcode.com/20xx/leaderboard/self
and it'll correlate that with that year's global stats
to generate statistics including percentiles.
"""
import argparse
import re
import sys
import math
import urllib.request

SITE_URL = "https://adventofcode.com/"

def errexit(msg, code=1):
   print("ERROR:" if code else "WARNING:", msg, file=sys.stderr)
   if code: sys.exit(code)

def getfile(filename):
   try:
      with open(filename, encoding='utf-8', errors='replace') as f:
         return f.read()
   except EnvironmentError as e:
      errexit(f"failed to read '{filename}' - {e}")

def try_int(x):
   try:
      if ':' in x:
         return sum(int(part) * radix for part, radix in zip(x.split(':')[::-1], (1, 60, 3600)))
      return int(x)
   except ValueError:
      return x

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=__doc__)
   parser.add_argument("infile", metavar="FILE",
                       help="input .html file with player statistics (no MHTML!)")
   parser.add_argument("--stats", metavar="FILE",
                       help="global statistics .html file, saved from .../<year>stats [default: download]")
   parser.add_argument("-o", "--output", metavar="FILE",
                       help="output .html file [default: write to stdout]")
   args = parser.parse_args()

   # open input
   html = getfile(args.infile)

   # heuristics: which year is it?
   years = set(re.findall(r'<a href="/(\d{4})/', html, flags=re.I))
   if len(years) != 1:
      errexit("missing or ambigous year information in source HTML")
   year = years.pop()

   # extract actual stats
   days = {}
   for m in re.finditer(r'''^
      \s* (?P<day> \d+)
      \s+ (?P<time1> \d+:\d\d:\d\d)
      \s+ (?P<rank1> \d+)
      \s+ (?P<score1> \d+)
      \s+ (?P<time2> \d+:\d\d:\d\d)
      \s+ (?P<rank2> \d+)
      \s+ (?P<score2> \d+)
   ''', html, flags=re.M+re.X):
      row = { k: try_int(v) for k,v in m.groupdict().items() }
      days[row['day']] = row
   if not days:
      errexit("no valid statistics data found in source HTML")

   # get stats HTML
   if args.stats:
      stats = getfile(args.stats)
   else:
      url = SITE_URL + year + "/stats"
      try:
         with urllib.request.urlopen(url) as f:
            stats = f.read()
      except EnvironmentError as e:
         errexit(f"failed to retrieve '{url}' - {e}")
      stats = stats.decode('utf-8', errors='replace')

   # parse stats HTML
   ok = set()
   for st_year, day, line in re.findall(r'<a href="/(\d+)/day/(\d+)">(.*?)</a>', stats, flags=re.I+re.S):
      if year != st_year: continue
      day = int(day)
      if not(day in days): continue
      try:
         total2, total1 = map(int, re.findall(r'<span[^>]+>\s*(\d+)', line, flags=re.I+re.S))
      except ValueError:
         continue
      days[day]['total1'] = total1 + total2
      days[day]['total2'] = total2
      ok.add(day)
   if not ok:
      errexit("no global statistics found", 0)
   elif ok != set(days):
      errexit("global statistics are incomplete", 0)

   # compute geometric mean
   mean = {}
   for d in days.values():
      for f, v in d.items():
         if isinstance(v, int):
            oa, oc = mean.get(f, (0,0))
            mean[f] = (oa + math.log(max(v, 1E-10)), oc + 1)
   d = days[0] = {}
   for f, (acc, cnt) in mean.items():
      d[f] = int(math.exp(acc / cnt) + 0.5)
   d["day"] = 0

   # compile result
   header = [
      "    | ---------------- Part 1 ---------------- | ---------------- Part 2 ----------------",
      "Day |     Time   Rank/Total  Percentile  Score |     Time   Rank/Total  Percentile  Score",
   ]
   res = [''.join([
      f"{d['day'] or 'Avg':3} | ",
      (f"{d['time1']//3600:2d}:{d['time1']//60%60:02d}:{d['time1']%60:02d} " if d.get('time1') else "  ----   "),
      f"{(d.get('rank1') or '---'):6}/",
      f"{(d.get('total1') or '---'):<6} ",
      (f"{d['rank1']/d['total1']*100:9.3f}% " if (d.get('rank1') and d.get('total1')) else '       --- '),
      f"{d.get('score1', 0):>6} | ",
      (f"{d['time2']//3600:2d}:{d['time2']//60%60:02d}:{d['time2']%60:02d} " if d.get('time2') else "  ----   "),
      f"{(d.get('rank2') or '---'):6}/",
      f"{(d.get('total2') or '---'):<6} ",
      (f"{d['rank2']/d['total2']*100:9.3f}% " if (d.get('rank2') and d.get('total2')) else '       --- '),
      f"{d.get('score2', 0):6}",
   ]) for d in sorted(days.values(), key=lambda d:-d['day'])]

   # generate output
   if args.output:
      # pretty-print headers
      hrange = [(m.start(0), m.end(0)) for m in re.finditer('-+[ part12]+-+', header[0], flags=re.I)]
      for cls, (start, end) in zip(("leaderboard-daydesc-both", "leaderboard-daydesc-first"), hrange[::-1]):
         for i in range(len(header)):
            header[i] = header[i][:start] + f'<span class="{cls}">' + header[i][start:end] + '</span>' + header[i][end:]
      # fix links, remove sidebar, compile and insert content
      html = re.sub(r'href="/', 'href="' + SITE_URL, html, flags=re.I)
      html = re.sub(r'<div id="sidebar".*</div><!--/sidebar-->', '', html, flags=re.I+re.S)
      article = """<article><p>
         These are your personal leaderboard times.<br>
         <em>Rank</em> is your position on that leaderboard:
         1 means you were the first person to get that star,
         2 means the second, 100 means the 100th, etc.<br>
         <em>Total</em> is the total number of participants who got
         the star in question.<br>
         The <em>percentile</em> is a measure of your performance relative to
         all other participants, i.e. how many other participants were quicker
         than you. A lower number is better.<br>
         <em>Score</em> is the number of points you got for your rank:
         100 for 1st, 99 for 2nd, ..., 1 for 100th, and 0 otherwise.<br>
         The <em>Avg</em> row gives an indication of the average times, rank,
         total participants and score as a <em>geometric mean</em> of the
         daily statistics.
      </p><pre>""" + '\n'.join(header + res) + "</pre></article>"
      html = re.sub('<article>(.*?)</article>', article, html, flags=re.I+re.S)
      # write file
      try:
         with open(args.output, 'w', encoding='utf-8', errors='replace') as f:
            f.write(html)
      except EnvironmentError as e:
         errexit(f"failed to write '{args.output}' - {e}")
   else:
      print('\n'.join(header + res))
