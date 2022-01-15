import zombiedice, random

class MyZombie:
    def __init__(self, name, variant):
        # all zombies must have a name
        self.name = name
        self.variant = variant
    
    def turn(self, gameState):
        dice_roll_results = zombiedice.roll() # initial roll
        brains = 0
        shotguns = 0

        if self.variant == 'random_after_first':
            while random.randint(0,1) and dice_roll_results is not None:
                dice_roll_results = zombiedice.roll()
        elif self.variant == 'stop_at_2_brains':
            while dice_roll_results is not None:
                brains += dice_roll_results['brains']
                if brains < 2:
                    dice_roll_results = zombiedice.roll()
                else:
                    break
        elif self.variant == 'stop_at_2_shotguns':
            while dice_roll_results is not None:
                shotguns += dice_roll_results['shotgun']
                if shotguns < 2:
                    dice_roll_results = zombiedice.roll()
                else:
                    break
        elif self.variant == 'init_decision_1-4_rolls_but_stop_at_2_shotguns':
            init_decision = random.randint(1,4)
            roll_count = 1
            while dice_roll_results is not None:
                shotguns += dice_roll_results['shotgun']
                if shotguns < 2 and roll_count < init_decision:
                    roll_count += 1
                    dice_roll_results = zombiedice.roll()
                else:
                    break
        elif self.variant == 'stop_at_more_shotguns_than_brains':
            while dice_roll_results is not None:
                brains += dice_roll_results['brains']
                shotguns += dice_roll_results['shotgun']
                if shotguns < brains:
                    dice_roll_results = zombiedice.roll()
                else:
                    break




zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stops at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stops at 1 Shotguns', minShotguns=1),
    MyZombie(name='Mine - Random After First', variant='random_after_first'),
    MyZombie(name='Mine - Stop at 2 Brains', variant='stop_at_2_brains'),
    MyZombie(name='Mine - Stop at 2 Shotguns', variant='stop_at_2_shotguns'),
    MyZombie(name='Mine - Init Decision 1-4 Rolls but Stop at 2 Shotguns', variant='init_decision_1-4_rolls_but_stop_at_2_shotguns'),
    MyZombie(name='Mine - Stop at More Shotguns Than Brains', variant='stop_at_more_shotguns_than_brains')
)

zombiedice.runTournament(zombies=zombies, numGames=1000)