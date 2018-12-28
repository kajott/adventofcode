#!/usr/bin/env python2
"""
check Python scripts (or a whole directory tree of them)
for a few(!) simple code golf possibilities
"""
import sys, os, re, collections, keyword

###############################################################################

def is_relevant_file(name):
    name = name.lower()
    return name.startswith("aoc") \
       and name.endswith(".py") \
       and not("_vis" in name) \
       and not("_trace" in name) \
       and not("_test" in name) \
       and not("nogolf" in name)

checkers = []
def checker(func):
    checkers.append(func)
    return func

def line_checker(lines, func):
    res = []
    for lineno, line in enumerate(lines):
        for start, end in func(line):
            res.append((lineno + 1, start, end, False))
    return res

def regex_checker(lines, regex):
    def main(line):
        for m in re.finditer(regex, line):
            gid = 1  # TODO
            yield (m.start(gid), m.end(gid))
    return line_checker(lines, main)

def whiten_strings(line):
    return re.sub(r'(["\'])(.*?[^\\])\1', lambda m: m.group(1) + '0' * (m.end(2) - m.start(2)) + m.group(1), line)

###############################################################################

@checker
def indent(data, lines):
    "block more indented than necessary"
    stack = [0]
    for n, line in enumerate(lines):
        indent = re.match(r'\s*', line).end(0)
        while stack and (indent < stack[-1]):
            stack.pop()
        if stack and (indent > stack[-1]):
            if indent > (stack[-1] + 1):
                yield (n+1, stack[-1] + 1, indent, False)
            stack.append(indent)

###############################################################################

@checker
def mergelines(data, lines):
    "line can be merged with previous line"
    indent = [re.match(r'\s*', line).end(0) for line in lines] + [0]
    block = [bool(re.search(r'\b(if|else|elif|for|while|with|try|except)\b', line)) for line in lines] + [False]
    colon = [line.rstrip().endswith(':') for line in lines] + [False]
    def has_subblocks(n):
        for i in xrange(n+1, len(lines)):
            if indent[i] < indent[n]: break
            if block[i]: return True
    for n in xrange(len(lines)):
        indent_delta = indent[n] - indent[n-1]
        if block[n]: continue  # can't merge a new block statement
        if not indent[n]: continue  # not indented, merging wouldn't save anything
        if indent_delta < 0: continue  # dedent, must not merge
        if (indent_delta > 0) and has_subblocks(n): continue  # inside new block, but more blocks are contained in it
        if (indent_delta == 0) and block[n-1] and not(colon[n-1]): continue  # same level, but previous line was a single-line block
        yield (n + 1, 0, indent[n], False)

###############################################################################

@checker
def extraspace(data, lines):
    "extra space between tokens"
    def main(line):
        i, llen = 1, len(line) - 1
        while i < llen:
            if not(line[i].isspace()):
                i += 1
                continue
            j = i + 1
            while (j <= llen) and line[j].isspace():
                j += 1
            l = line[i-1]
            r = line[j]
            if not((l in _es_left) and (r in _es_right)) \
            and not((l+r) in ("0x", "0o", "0b")):
                yield (i, j)
            i = j
    return line_checker(lines, main)
_alpha = "abcdefghijklmnopqrstuvwxyz"
_alpha += _alpha.upper() + "_"
_es_left = set(_alpha + " \t\r\n\f\v")
_es_right = set(_alpha + "0123456789")

###############################################################################

@checker
def comporder(data, lines):
    "can eliminate whitespace by swapping comparison order"
    return regex_checker(lines, r'[a-zA-Z0-9_](\s+\w+([=!]=|<=?|>=?)([\'"]).*?\3)[^a-zA-Z_]')

###############################################################################

@checker
def methodname(data, lines):
    "operator can be used instead of method"
    return regex_checker(lines, r'(\.(append|extend|update|add|(union|difference|intersection)(_update)?))')

###############################################################################

@checker
def alias(data, lines):
    "long identifier can be aliased"
    location = {}
    freq = collections.defaultdict(int)
    for m in re.finditer('\.?([a-zA-Z]\w+)', data):
        name = m.group(1)
        if name in _kwset: continue
        freq[name] += 1
        if not(name in location):
            location[name] = (m.start(0), m.end(0))
    for name, freq in freq.iteritems():
        l = len(name)
        if (freq + l + 3) < (freq * l):
            s, e = location[name]
            yield (0, s, e, True)
_kwset = set(keyword.kwlist)

###############################################################################

def check_file(filename):
    data = open(filename, "rb").read()
    lines = data.split('\n')
    if not lines[-1]: del lines[-1]
    clean_lines = map(whiten_strings, lines)
    clean_data = '\n'.join(clean_lines) + '\n'
    res = []
    for ckidx, checker in enumerate(checkers):
        for lineno, start, end, hide in checker(clean_data, clean_lines):
            if not lineno:
                while (lineno < len(lines)) and (start > len(lines[lineno])):
                    l = len(lines[lineno]) + 1
                    start, end = start - l, end - l
                    lineno += 1
                lineno += 1
            if (lineno < 1) or (lineno > len(lines)):
                lineno = 0
            res.append((0 if hide else lineno, ckidx, -start * (lineno > 0), lineno, start, end, hide))
    if not res:
        return
    res.sort()
    res.append((-1, -1, -1, -1, -1, -1, True))
    last = (-1, -1, True)
    hiline = None
    for sortline, ckidx, sortkey, lineno, start, end, hide in res:
        curr = (lineno, ckidx, hide)
        if curr != last:
            last_ln, last_ckidx, last_hide = last
            if last_ckidx >= 0:
                loc = filename
                if hiline and not(last_hide):
                    loc += ":%d" % last_ln
                print "\x1b[100;95m%s: \x1b[91m(%s)\x1b[37m %s\x1b[K\x1b[0m" % (loc, checkers[last_ckidx].__name__, checkers[last_ckidx].__doc__)
                if hiline:
                    print "\x1b[35m> \x1b[0m" + hiline
                print
            if ckidx < 0:
                break
            hiline = lines[lineno - 1] if lineno else None
        if hiline:
            hiline = hiline[:start] + "\x1b[41;97m" + hiline[start:end] + "\x1b[0m" + hiline[end:]
        last = curr


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        for f in sorted(args):
            check_file(os.path.normpath(f))
    else:
        for root, dirs, files in os.walk('.'):
            dirs.sort()
            for f in sorted(files):
                if is_relevant_file(f):
                    check_file(os.path.normpath(os.path.join(root, f)))
