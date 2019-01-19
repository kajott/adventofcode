import re, heapq

DEBUG = 0

PLAYER_HP_DECAY = 1  # 1 for part 2

PLAYER_INITIAL_HP, PLAYER_INITIAL_MANA = 50, 500
BOSS_INITIAL_HP, BOSS_DAMAGE = map(int, re.findall('\d+', open("input.txt").read()))


#PLAYER_INITIAL_HP, PLAYER_INITIAL_MANA, BOSS_INITIAL_HP, BOSS_DAMAGE = 10, 250, 13, 8


class GameState(object):
    @staticmethod
    def initial():
        new = GameState()
        new.turn = 0
        new.mana = PLAYER_INITIAL_MANA
        new.mana_spent = 0
        new.player_hp = PLAYER_INITIAL_HP
        new.boss_hp = BOSS_INITIAL_HP
        new.shield_timeout = 0
        new.poison_timeout = 0
        new.recharge_timeout = 0
        return new

    def copy(self, spend_mana=0):
        new = GameState()
        new.turn             = self.turn
        new.mana             = self.mana - spend_mana
        new.mana_spent       = self.mana_spent + spend_mana
        new.player_hp        = self.player_hp
        new.boss_hp          = self.boss_hp
        new.shield_timeout   = self.shield_timeout
        new.poison_timeout   = self.poison_timeout
        new.recharge_timeout = self.recharge_timeout
        return new

    def __str__(self):
        s = "%s's turn; player: %d HP, %d mana (%d spent); boss: %d HP" % (("player", "boss")[self.turn], self.player_hp, self.mana, self.mana_spent, self.boss_hp)
        if self.shield_timeout: s += "; shield-%d" % self.shield_timeout
        if self.poison_timeout: s += "; poison-%d" % self.poison_timeout
        if self.recharge_timeout: s += "; recharge-%d" % self.recharge_timeout
        return s

    def generate_turns(self):
        # terminal state?
        if (self.player_hp <= 0) or (self.boss_hp <= 0):
            return
    
        # copy this state to apply effects
        base = self.copy()
        base.turn = 1 - self.turn

        # apply player HP decay
        if base.turn:
            base.player_hp -= PLAYER_HP_DECAY
            if base.player_hp <= 0:
                if DEBUG: "  - player died of decay =>", base
                yield base
                return

        # apply effects
        if base.shield_timeout:
            armor = 7
            base.shield_timeout -=1
        else:
            armor = 0
        if base.poison_timeout:
            base.boss_hp -= 3
            base.poison_timeout -= 1
        if base.recharge_timeout:
            base.mana += 101
            base.recharge_timeout -= 1

        # boss may have died of poison
        if base.boss_hp <= 0:
            if DEBUG: print "  - boss died =>", base
            yield base
            return

        # process boss' turn
        if self.turn:
            base.player_hp -= max(1, BOSS_DAMAGE - armor)
            if DEBUG: print "  - boss attacks =>", base
            yield base
            return
        
        # magic missile
        t = base.copy(53)
        if t.mana >= 0:
            t.boss_hp -= 4
            if DEBUG: print "  - Magic Missile =>", t
            yield t

        # drain
        t = base.copy(73)
        if t.mana >= 0:
            t.boss_hp -= 2
            t.player_hp += 2
            if DEBUG: print "  - Drain =>", t
            yield t

        # shield
        t = base.copy(113)
        if (t.mana >= 0) and not(t.shield_timeout):
            t.shield_timeout = 6
            if DEBUG: print "  - Shield =>", t
            yield t

        # poison
        t = base.copy(173)
        if (t.mana >= 0) and not(t.poison_timeout):
            t.poison_timeout = 6
            if DEBUG: print "  - Poison =>", t
            yield t

        # recharge
        t = base.copy(229)
        if (t.mana >= 0) and not(t.recharge_timeout):
            t.recharge_timeout = 5
            if DEBUG: print "  - Recharge =>", t
            yield t


state = GameState.initial()
q = [(0, state)]
while state.boss_hp > 0:
    cost, state = heapq.heappop(q)
    if DEBUG: print "*", state
    for substate in state.generate_turns():
        heapq.heappush(q, (substate.mana_spent, substate))    
print cost
