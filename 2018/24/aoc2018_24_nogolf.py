DEBUG = 1
# 0 = silent
# 1 = print match summary
# 2 = report as in example

import re, collections

data = """
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
""".split('\n')
data = open("input.txt")

team_names = {0:"no teams"}

class Group(object):
    def __init__(self, team, no, units, hp, attack, damage, initiative):
        self.team = team
        self.no = no
        self.units = units
        self.hp = hp
        self.attack = attack
        self.damage = damage
        self.initiative = initiative
        self.modifiers = collections.defaultdict(lambda: 1)
        self.power = units * damage

    def copy(self, boost=0):
        g = Group(self.team, self.no, self.units, self.hp, self.attack, self.damage + boost, self.initiative)
        g.modifiers = self.modifiers
        return g

    def set_modifier(self, scale, attacks):
        if attacks:
            for a in attacks.strip().split(','):
                self.modifiers[a.strip()] = scale

    def __str__(self):
        mods = []
        m = sorted(k for k,s in self.modifiers.iteritems() if s==2)
        if m: mods.append("weak to " + ', '.join(m))
        m = sorted(k for k,s in self.modifiers.iteritems() if s==0)
        if m: mods.append("immune to " + ', '.join(m))
        mods = " (%s)" % '; '.join(mods) if mods else ""
        return "[%s #%d] %d units each with %d hit points%s with an attack that does %d %s damage at initiative %d" \
             % (team_names[self.team], self.no, self.units, self.hp, mods, self.damage, self.attack, self.initiative)

    def sortkey_targetsel(self):
        return (-self.power, -self.initiative)
    def sortkey_attack(self):
        return -self.initiative


def print_header(msg):
    print (" %s " % msg).center(79, '-')
    print

def print_group_stats():
    for team in (1,2):
        print team_names[team] + ':'
        tgs = [g for g in groups if g.team == team]
        if tgs:
            for g in sorted(tgs, key=lambda g: g.no):
                print "Group %d contains %d units" % (g.no, g.units)
        else:
            print "No groups remain."
    print


def simulate_round(n):
    global groups

    if DEBUG >= 2:
        print_header("round %d" % n)
        print_group_stats()

    # clear all target selections
    for g in groups:
        g.target = None
        g.targeted = False
    total_targets = 0

    # target selection
    for g in sorted(groups, key=Group.sortkey_targetsel):
        try:
            damage, d1, d2, t = \
                max((g.power * t.modifiers[g.attack], t.power, t.initiative, t) \
                    for t in groups if not(t.targeted) and t.team != g.team)
        except ValueError:
            damage, t = 0, None  # no attackable group
        if damage and t:
            g.target = t
            t.targeted = True
            total_targets += 1
            if DEBUG >= 2:
                print team_names[g.team], "group", g.no, "would deal defending group", g.target.no, damage, "damage"
    if DEBUG >= 2: print

    # attack
    for g in sorted(groups, key=Group.sortkey_attack):
        t = g.target
        if not t: continue
        kill = min(t.units, g.power * t.modifiers[g.attack] / t.hp)
        t.units -= kill
        if DEBUG >= 2:
            print team_names[g.team], "group", g.no, "attacks defending group %d," % g.target.no, "killing", kill, "units"
        t.power = t.units * t.damage
    if DEBUG >= 2: print

    # remove dead groups
    groups = [g for g in groups if g.units > 0]
    return total_targets


def simulate_match(boost=0):
    global groups
    orig_groups = groups
    groups = [g.copy(boost * (g.team == 1)) for g in groups]
    if DEBUG >= 2:
        print_header("simulating match with boost %d" % boost)
    rounds = 0
    while True:
        survivors = set(g.team for g in groups)
        if len(survivors) < 2:
            break
        rounds += 1
        if not simulate_round(rounds):
            break  # stalemate detected
    if DEBUG >= 2:
        print_header("end of match")
        print_group_stats()
    if len(survivors) == 1:
        survivors = survivors.pop()
    else:
        survivors = 0
    units_left = sum(g.units for g in groups)
    if DEBUG >= 1:
        print "at boost %d, %s win after %d rounds with %d units left" % (boost, team_names[survivors], rounds, units_left)
        if DEBUG >= 2:
            print
    groups = orig_groups
    return (survivors, units_left)


groups = []
team = 0
no = 0
for line in data:
    if line.strip().endswith(':'):
        team += 1
        team_names[team] = line.strip()[:-1]
        no = 0
    m = re.match(r'(\d+) units each with (\d+) hit points( \((?P<m>.*?)\))? with an attack that does (?P<as>\d+) (?P<at>.*?) damage at initiative (?P<i>\d+)', line)
    if m:
        no += 1
        g = Group(team, no, int(m.group(1)), int(m.group(2)), m.group('at'), int(m.group('as')), int(m.group('i')))
        m = m.group('m')
        if m:
            for m in map(str.strip,m.split(';')):
                if m.startswith("weak to "):
                    g.set_modifier(2, m[8:])
                elif m.startswith("immune to "):
                    g.set_modifier(0, m[10:])
                else:
                    assert 0
        groups.append(g)

if DEBUG >= 2:
    for g in groups:
        print g
    print

winner = 0
boost = -1
while winner != 1:
    boost += 1
    winner, left = simulate_match(boost)
