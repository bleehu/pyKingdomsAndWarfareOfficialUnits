"""Official Kingdoms & Warfare unit traits, in alphabetical order.

Import this module and reference traits by constant, e.g. ``Traits.ADAPTABLE``.
"""

from KingdomsAndWarfare.Traits.Trait import Trait

AAAUUUGH = Trait(
    "AAAUUUGH!!!",
    "When this unit breaks, all adjacent units suffer 1 casualty.",
).homebrew = False

ADAPTABLE = Trait(
    "Adaptable",
    "This unit has advantage on Morale and Command tests.",
).homebrew = False

AERIAL_BOMBARDMENT = Trait(
    "Aerial Bombardment",
    "If this unit spends an activation doing nothing, it can use its next activation to target a fortification by making a DC 13 Power test. On a success, it deals 1d4 + 2 damage to the fortification.",
).homebrew = False

AMPHIBIOUS = Trait(
    "Amphibious",
    "This unit does not suffer movement penalties when fighting underwater, or in rain or mud.",
).homebrew = False

ARCADIAN = Trait(
    "Arcadian",
    "This unit has advantage on Power tests to resist battle magic.",
).homebrew = False

ARCHERS = Trait(
    "Archers",
    "This unit can attack any opposed unit. Successful Power tests the unit makes against opposed units that are not exposed inflict only 1 casualty.",
).homebrew = False

ARMORED_CARAPACE = Trait(
    "Armored Carapace",
    "This unit suffers no casualties from artillery Attack tests.",
).homebrew = False

BARBS = Trait(
    "Barbs",
    "An opposed infantry unit that makes a successful Power test as part of an attack against this unit suffers 1 casualty.",
).homebrew = False

BATTLE_HYMN = Trait(
    "Battle Hymn",
    "This unit has a bonus to Morale equal to its commander’s domain size, as do allied units while adjacent to this unit.",
).homebrew = False

BETTER_THAN_ONE = Trait(
    "Better than One",
    "When this unit attacks an opposed unit, it can also attack any other adjacent opposed unit.",
).homebrew = False

BIG = Trait(
    "Big",
    "This unit has advantage on Power tests against units whose casualties are lower than this unit’s.",
).homebrew = False

BLANKET_FIRE = Trait(
    "Blanket Fire",
    "As an action, choose a rank on the battlefield. Attack each unit in that rank. Recharge 4–6.",
).homebrew = False

BLINDING = Trait(
    "Blinding",
    "When an opposed unit fails an Attack test against this unit, the opposed unit is disoriented.",
).homebrew = False

BURNING = Trait(
    "Burning",
    "Each opposed unit that activates adjacent to this unit suffers 1 casualty.",
).homebrew = False

BURROW = Trait(
    "Burrow",
    "As an action, remove this unit from the battlefield. On its next activation, place the unit in any empty space. The unit is disoriented until the end of that activation.",
).homebrew = False

CHAOS_VULNERABILITY = Trait(
    "Chaos Vulnerability",
    "This unit has disadvantage on Power tests to resist battle magic.",
).homebrew = False

CHARGE = Trait(
    "Charge",
    "If this unit moves at least 1 space before it attacks, it has advantage on Attack tests for this activation as long as the target is in the direction the unit moved.",
).homebrew = False

CHORUS_OF_VICTORY = Trait(
    "Chorus of Victory",
    "As an action, choose a rank on the battlefield. Each allied unit in that rank increments its casualty die and has advantage on Attack tests until the end of its next activation. Recharge 6.",
).homebrew = False

CLOSE_RANGE = Trait(
    "Close Range",
    "This unit has advantage on Attack tests and Power tests against adjacent units.",
).homebrew = False

CLOUD_OF_DARKNESS = Trait(
    "Cloud of Darkness",
    "Opposed units have disadvantage on Attack tests against this unit.",
).homebrew = False

COLLATERAL_DAMAGE = Trait(
    "Collateral Damage",
    "When this unit makes a successful Power test against an infantry or artillery unit, the unit opposite the target also suffers 1 casualty.",
).homebrew = False

CONSUME = Trait(
    "Consume",
    "As an action, this unit targets an opposed unit with lower casualties than it that it can attack. The target must succeed on a DC 15 Power test or break. Recharge 5–6.",
).homebrew = False

CORRODE = Trait(
    "Corrode",
    "When this unit makes a successful Attack test against an opposed unit, that unit takes −2 to Attack and Defense. Each opposed unit can be affected by this trait only once per battle.",
).homebrew = False

CORROSIVE_BREATH = Trait(
    "Corrosive Breath",
    "As an action, choose three adjacent opposed units. Each unit must succeed on a Power test (DC = 8 + this unit’s size) or suffer 2 casualties and gain one acid token. The acid token inflicts 1 casualty. Recharge 5–6.",
).homebrew = False

CREATE_DEAD = Trait(
    "Create Dead",
    "If this unit causes an opposed unit to break, replace that unit with a Ghoul Infantry unit under the command of this unit’s commander. The new unit can act on the commander’s next turn.",
).homebrew = False

DAMAGE_RESISTANT = Trait(
    "Damage Resistant",
    "Successful Attack tests against this unit inflict no casualties. Successful Power tests inflict casualties normally.",
).homebrew = False

DAYLIGHT_WEAKNESS = Trait(
    "Daylight Weakness",
    "While in direct sunlight, this unit has disadvantage on Power tests.",
).homebrew = False

DEAD = Trait(
    "Dead",
    "This unit always succeeds on Morale tests, and cannot be diminished.",
).homebrew = False

DIG = Trait(
    "“Dig!”",
    "As an action, choose a space containing an opposed fortification and remove this unit from the battlefield. On the unit’s next activation, the target fortification takes 2d6 damage and this unit breaks as though it were in that space.",
).homebrew = False

DIRE_HYENA_MOUNTS = Trait(
    "Dire Hyena Mounts",
    "This unit has advantage on Attack tests against diminished units.",
).homebrew = False

DISRUPTIVE = Trait(
    "Disruptive",
    "When an opposed unit adjacent to this unit activates, it has a 25 percent chance of doing nothing on that activation.",
).homebrew = False

DRACONIC_ANCESTRY = Trait(
    "Draconic Ancestry",
    "This unit cannot be disorganized or weakened, and it is immune to the Harrowing trait.",
).homebrew = False

DRAGONKIN = Trait(
    "Dragonkin",
    "If there is an allied dragon in the battle or if this unit’s commander has some sort of draconic ancestry, this unit has advantage on Attack tests, Command tests, and Morale tests.",
).homebrew = False

DRONE = Trait(
    "Drone",
    "As an action, choose a rank on the battlefield. Each opposed unit in that rank must succeed on a DC 15 Power test or suffer 1 casualty and be unable to move on its next activation. This unit can use this trait only once per battle.",
).homebrew = False

ELF_SHOT = Trait(
    "Elf-shot",
    "When this unit succeeds on a Power test as part of an attack, the target unit must succeed on a DC 10 Power test or become weakened until the end of its next activation.",
).homebrew = False

EMBIGGEN = Trait(
    "Embiggen",
    "As a reaction to activating, this unit’s size increases to 8. Its casualty die becomes a d8 and is incremented twice. Until the end of its activation, the unit has advantage on Attack tests and Power tests. This unit can use this trait only once per battle.",
).homebrew = False

ETERNAL = Trait(
    "Eternal",
    "This unit has advantage on Morale tests against undead or fiend units, and on the Morale test to attack units with the Harrowing trait.",
).homebrew = False

ETHEREAL = Trait(
    "Ethereal",
    "This unit has +1 to movement. It can move through other units, but only if it can end its movement in an empty space. Other units do not gain bonuses to Defense from fortifications against this unit’s attacks.",
).homebrew = False

FADE = Trait(
    "Fade",
    "After a successful Attack test, this unit can move back 1 space. Opposed units cannot use the Follow Up maneuver in response.",
).homebrew = False

FAST_SIEGE_WEAPON = Trait(
    "Fast Siege Weapon",
    "This unit can attack a fortification. It automatically hits (no Attack test or Power test needed) and deals 3 damage.",
).homebrew = False

FAST_SIEGE_WEAPON_HEAVY = Trait(
    "Fast Siege Weapon (Heavy)",
    "This unit can attack a fortification. It automatically hits (no Attack test or Power test needed) and deals 5 damage.",
).homebrew = False

FEARLESS = Trait(
    "Fearless",
    "This unit automatically succeeds on Morale tests.",
).homebrew = False

FEARSOME = Trait(
    "Fearsome",
    "As a reaction to making an Attack test, this unit forces the target to succeed on a Morale test (DC = 8 + this unit’s size) or suffer 1 additional casualty.",
).homebrew = False

FEAST = Trait(
    "Feast",
    "At the end of this unit’s activation, if any diminished unit is adjacent to it, increment this unit’s casualty die.",
).homebrew = False

FIRE_BLAST = Trait(
    "Fire Blast",
    "As an action, this unit forces two adjacent opposed units to each make a DC 13 Power test. On a failure, a unit suffers 2 casualties. Recharge 5–6.",
).homebrew = False

FIRE_BREATH = Trait(
    "Fire Breath",
    "As an action, this unit forces three adjacent opposed units to each make a Power test (DC = 8 + this unit’s size). On a failure, a unit suffers 2 casualties and gains a fire token. The fire token inflicts 1 casualty. Recharge 5–6.",
).homebrew = False

FIRE_IMMUNITY = Trait(
    "Fire Immunity",
    "This unit does not suffer casualties from traits or other effects with “burning,” “fire,” or “flame” in their names, or from fire tokens.",
).homebrew = False

FLAMING_WEAPONS = Trait(
    "Flaming Weapons",
    "When this unit makes a successful Power test as part of an attack, it adds a fire token to the target in addition to the normal effects of the test. The fire token inflicts 1 casualty.",
).homebrew = False

FOLLOW_THE_STANDARD = Trait(
    "“Follow the Standard!”",
    "When this unit succeeds on a Power test as part of an attack, each cavalry unit the unit’s commander controls can use a reaction to immediately make an attack against the target of the Power test.",
).homebrew = False

GUERRILLAS = Trait(
    "Guerrillas",
    "When this unit succeeds on an Attack test against any opposed infantry or artillery unit (but not siege weapons), that unit is disoriented.",
).homebrew = False

GULP = Trait(
    "Gulp",
    "As an action, this unit forces an opposed infantry or artillery unit (but not a siege engine) to make a DC 15 Power test. On a failure, the target unit is diminished (or is broken if it was already diminished). Recharge 5–6.",
).homebrew = False

HALLUCINATORY_SPORES = Trait(
    "Hallucinatory Spores",
    "As an action, this unit forces a legal target to make a DC 15 Power test. On a failure, the opposed unit attacks one of its own allied units of this unit’s choice on the opposed unit’s next activation.",
).homebrew = False

HARD_HATS = Trait(
    "Hard Hats",
    "This unit has +2 to Defense against attacks from aerial units.",
).homebrew = False

HARRIERS = Trait(
    "Harriers",
    "If this unit succeeds on a Power test as part of an attack, this unit becomes the target unit’s only legal target on its next activation.",
).homebrew = False

HARROWING = Trait(
    "Harrowing",
    "Any opposed infantry, cavalry, or aerial unit must first succeed on a Morale test (DC = 10 + this unit’s tier) when it attacks this unit. On a success, the attacking unit is not affected by any unit’s Harrowing trait for the rest of the battle. On a failure, the attacking unit’s activation ends.",
).homebrew = False

HEROES_OF_THE_MYRIAD_WORLDS = Trait(
    "Heroes of the Myriad Worlds",
    "Once per battle as a bonus action, this unit can gain advantage on Attack tests and Power tests until the end of its activation.",
).homebrew = False

HOLY = Trait(
    "Holy",
    "Undead and fiend units have disadvantage on Attack tests and Power tests against this unit.",
).homebrew = False

HOP = Trait(
    "Hop",
    "For its movement, this unit can move to any empty space on the battlefield.",
).homebrew = False

IMPLACABLE = Trait(
    "Implacable",
    "This unit cannot unwillingly be moved or teleported, and it can ignore any effects of terrain.",
).homebrew = False

INDISTINCT = Trait(
    "Indistinct",
    "Attack tests for ranged attacks made against this unit have disadvantage.",
).homebrew = False

INEXORABLE = Trait(
    "Inexorable",
    "This unit is immune to any effect that would hinder or stop its movement, or that would deny it the ability to use actions.",
).homebrew = False

INSPIRE_FEAR = Trait(
    "Inspire Fear",
    "Whenever this unit leaves an opposed unit diminished, all goblinoid units in the same rank as this unit can immediately attack a legal target.",
).homebrew = False

INTO_THE_BREACH = Trait(
    "Into the Breach",
    "When this unit successfully executes the Follow Up maneuver, it has +2 bonus to Defense until the beginning of its next activation.",
).homebrew = False

INVISIBILITY = Trait(
    "Invisibility",
    "This unit cannot be attacked until it successfully attacks an opposed unit.",
).homebrew = False

JAUNT = Trait(
    "Jaunt",
    "In place of its movement, remove this unit from the battlefield. It returns to the space it left, or an unoccupied space of the GM’s choice if that space is occupied, at the start of its next activation. Recharge 5–6.",
).homebrew = False

LIGHTNING_BREATH = Trait(
    "Lightning Breath",
    "As an action, choose a rank on the battlefield. Each unit in that rank must succeed on a Power test (DC = 8 + this unit’s size) or suffer 2 casualties. Recharge 5–6.",
).homebrew = False

LOAD_THE_BONES = Trait(
    "Load the Bones!",
    "While any diminished unit is adjacent to this unit, this unit has +2 damage against opposed fortifications.",
).homebrew = False

MAGIC_RESISTANT = Trait(
    "Magic Resistant",
    "This unit has advantage on Power tests to resist battle magic.",
).homebrew = False

MAGICAL_ADEPTS = Trait(
    "Magical Adepts",
    "As a bonus action, this unit forces an opposed unit to make a DC 13 Power Test. On a failure, allied units have advantage on Attack tests against the opposed unit until the end of the battle. Recharge 5–6.",
).homebrew = False

MANEUVER_DETONATE = Trait(
    "Maneuver: Detonate",
    "As an action, this unit deals 1d4 + 2 damage to an adjacent fortification. Recharge 3–6.",
).homebrew = False

MANEUVER_EVASIVE_MANEUVERS = Trait(
    "Maneuver: “Evasive Maneuvers!”",
    "As a reaction when an opposed artillery unit makes an Attack test against this unit, impose disadvantage on the opposed unit’s Attack test. Recharge 5–6.",
).homebrew = False

MANEUVER_FIRE = Trait(
    "Maneuver: “Fire!!”",
    "As a reaction to a successful Power test made against a target unit, add a fire token to the target. The fire token inflicts 1 casualty. Recharge 4–6.",
).homebrew = False

MANEUVER_HOLD_THE_LINE = Trait(
    "Maneuver: “Hold the Line!”",
    "As a reaction to being diminished, this unit makes a DC 13 Command test. On a success, this unit ignores the casualties that caused it to become diminished, and is not diminished.",
).homebrew = False

MANEUVER_LANCERS_FLANK_THEM = Trait(
    "Maneuver: “Lancers! Flank Them!”",
    "As a reaction when an opposed cavalry or aerial unit inflicts 1 or more casualties on an allied infantry or artillery unit, this unit makes a free attack against that opposed unit.",
).homebrew = False

MANEUVER_LAND_AND_CHARGE = Trait(
    "Maneuver: “Land and Charge!”",
    "While this unit has the aerial type, it can use a bonus action to make a DC 11 Command test. On a success, this unit’s Power tests have +2 damage on this activation, but the unit’s type becomes cavalry. At the end of its next activation, the unit regains the aerial type. Recharge 4–6.",
).homebrew = False

MANEUVER_OUTFLANK = Trait(
    "Maneuver: Outflank",
    "As an action, move this unit into any empty space. Any opposed unit that executes the Follow Up maneuver in response has disadvantage on the Command test.",
).homebrew = False

MANEUVER_PREY_ON_THE_WEAK = Trait(
    "Maneuver: “Prey on the Weak.”",
    "As a reaction to an exposed opposed unit being diminished, this unit makes a DC 10 Command test. On a success, the unit makes an attack against the opposed unit.",
).homebrew = False

MANEUVER_REPAIR = Trait(
    "Maneuver: Repair",
    "As an action, a fortification this unit is on or adjacent to recovers 1d4 + 2 hit points, up to its starting hit points.",
).homebrew = False

MANEUVER_SPIT_UPON_THEIR_HORNS = Trait(
    "Maneuver: “Spit Upon Their Horns.”",
    "As a reaction to succeeding on a Power test made as part of an attack, this unit makes a DC 13 Command test. On a success, the target unit suffers 1 additional casualty.",
).homebrew = False

MANEUVER_STRAFE = Trait(
    "Maneuver: Strafe",
    "As a reaction to succeeding on a Power test made as part of an attack against an opposed artillery or infantry unit, this unit makes a DC 13 Command test. On a success, two adjacent opposed units in the same rank as the target unit each suffer 1 casualty.",
).homebrew = False

MANEUVER_TESTUDO = Trait(
    "Maneuver: Testudo",
    "As a reaction to suffering 1 or more casualties from an opposed artillery or aerial unit’s Attack test, this unit makes a DC 13 Command test. On a success, any opposed unit targeting this unit has disadvantage on Power tests until this unit’s next activation.",
).homebrew = False

MASS_PROTECTION_AGAINST_EVIL = Trait(
    "Mass Protection Against Evil",
    "Any opposed infantry or artillery unit must succeed on a DC 15 Morale test to enter the vanguard rank of this unit’s side.",
).homebrew = False

MELD = Trait(
    "Meld",
    "As a reaction to a successful Attack test against an infantry or artillery unit, this unit can move into the target unit’s space. While this unit is in the target’s space, the target unit cannot move and can attack only this unit. Units attacking either unit in this space have a 50 percent chance of targeting the wrong unit.",
).homebrew = False

MOBILE = Trait(
    "Mobile",
    "This unit has advantage on the Command test when using the Follow Up maneuver, and can move back 2 spaces when using the Withdraw maneuver.",
).homebrew = False

NATURES_BOND = Trait(
    "Nature’s Bond",
    "When an allied infantry or artillery unit suffers 1 or more casualties, this unit can take the casualty instead. This unit must deploy in its side’s front.",
).homebrew = False

NONE = Trait(
    "None",
    "This unit has no traits.",
).homebrew = False

NOXIOUS_FOG = Trait(
    "Noxious Fog",
    "As an action, this unit places two poison tokens in each of 4 adjacent spaces. Any unit that moves into a space with one or more of these poison tokens or that activates there suffers 1 casualty per token. Each space loses one poison token at the end of this unit’s subsequent activations. Recharge 5–6.",
).homebrew = False

PACK_TACTICS = Trait(
    "Pack Tactics",
    "When an adjacent unit that also has this trait successfully uses the Follow Up maneuver (page 109), this unit can move into any empty space adjacent to this unit’s current position.",
).homebrew = False

PIKE_TRAINING = Trait(
    "Pike Training",
    "This unit automatically succeeds on Command test for the Set for Charge manuever.",
).homebrew = False

POINT_BLANK = Trait(
    "Point Blank",
    "When this unit succeeds on a Power test as part of an attack against an adjacent unit, it inflicts 1 additional casualty.",
).homebrew = False

POISONOUS = Trait(
    "Poisonous",
    "When this unit succeeds on a Power test as part of an attack, the target unit is also weakened until the end of its next activation.",
).homebrew = False

POOL_OF_SOULS_BLOOD = Trait(
    "Pool of Soul’s Blood",
    "Any opposed infantry or artillery unit adjacent to this unit cannot leave its space.",
).homebrew = False

QUADRUPED = Trait(
    "Quadruped",
    "For its movement, this unit becomes a cavalry unit until the end of its activation. The unit leaves the grid and then returns to the space it left at the end of its activation (or to its army’s reserve rank if that space is occupied). Recharge 5–6.",
).homebrew = False

RAM_RIDERS = Trait(
    "Ram Riders",
    "When this unit succeeds on a Power test as part of an attack, the target unit must succeed on a followup DC 10 Power test or become disoriented until the end of its next activation.",
).homebrew = False

RECKLESS = Trait(
    "Reckless",
    "This unit can take disadvantage on any Attack test in order to have that Attack test inflict an additional 1 casualty.",
).homebrew = False

REFLECTOR = Trait(
    "Reflector",
    "When this unit fails a Power test against a wand, it can use a reaction to roll a d20. On a 10 or higher, this unit suffers no effect from the wand and the unit activating the wand suffers the effect instead.",
).homebrew = False

REGENERATE = Trait(
    "Regenerate",
    "Each time this unit activates, increment its casualty die by 1.",
).homebrew = False

RELENTLESS = Trait(
    "Relentless",
    "As a reaction to suffering a casualty that would cause this unit to break, this unit makes a DC 13 Power test. On a success, this unit does not break and has 1 casualty.",
).homebrew = False

RIME = Trait(
    "Rime",
    "Any opposed infantry or artillery unit adjacent to this unit has its movement reduced to 0 and cannot benefit from bonus movement.",
).homebrew = False

ROCK = Trait(
    "Rock!",
    "As an action, this unit can make an Attack test against any opposed unit, with disadvantage if the target is an aerial unit. Recharge 4–6.",
).homebrew = False

ROCKBREAKER = Trait(
    "Rockbreaker",
    "This unit deals double damage against fortifications.",
).homebrew = False

ROLLING_THUNDER = Trait(
    "Rolling Thunder",
    "As an action, this unit makes an opposed Power test against an adjacent opposed unit. If this unit’s result is equal to or greater than the target’s, the target unit must move back 1 space or break. This unit immediately moves into the target unit’s vacated space.",
).homebrew = False

RUSH = Trait(
    "Rush",
    "This unit automatically succeeds on the Command test for the Follow Up maneuver.",
).homebrew = False

SAVAGE = Trait(
    "Savage",
    "Each successful Attack test by this unit adds a bleed token to a target unit. Each bleed token inflicts 2 casualties.",
).homebrew = False

SCOURGE_OF_THE_WILD = Trait(
    "Scourge of the Wild",
    "This unit has +2 to Attack and +2 to Power against orc, goblinoid, or elf units.",
).homebrew = False

SCOUTS = Trait(
    "Scouts",
    "This unit can deploy into the rear rank of an opposed army.",
).homebrew = False

SCREECH = Trait(
    "Screech",
    "As an action, this unit forces an opposed unit to succeed on a DC 15 Power test or become misled. Recharge 4–6.",
).homebrew = False

SHOCK_TROOPS = Trait(
    "Shock Troops",
    "Each time this unit causes another unit to be diminished, this unit gains +2 to Attack and +2 to Power until the end of the battle.",
).homebrew = False

SIEGE_ENGINE = Trait(
    "Siege Engine",
    "This unit must spend 1 round of battle doing nothing before each attack. This unit can attack a fortification. It automatically hits (no Attack test or Power test needed) and deals 1d4 + 2 damage.",
).homebrew = False

SIEGE_WEAPON = Trait(
    "Siege Weapon",
    "This unit can attack an adjacent fortification. It automatically hits (no Attack test or Power test needed) and deals 3 damage.",
).homebrew = False

SLAM = Trait(
    "Slam",
    "When this unit succeeds on a Power test as part of an attack, the target unit is also disoriented.",
).homebrew = False

SMOKE_SCREEN = Trait(
    "Smoke Screen",
    "When this unit succeeds on an Attack test against another unit, that unit is also disoriented.",
).homebrew = False

SOLAR_FLARE = Trait(
    "Solar Flare",
    "Once per battle as a reaction to targeting a fortification, the damage this unit deals to fortifications is maximized, and it deals that damage to all fortifications in one rank.",
).homebrew = False

SOPORIFIC_SPORES = Trait(
    "Soporific Spores",
    "As an action, this unit forces a legal target to make a DC 13 Power test. On a failure, the opposed unit is disorganized.",
).homebrew = False

SOW_CHAOS = Trait(
    "Sow Chaos",
    "Each opposed unit within 1 space of this unit has disadvantage on Morale and Command tests, and suffers 1 additional casualty if it fails the Morale test to avoid becoming diminished.",
).homebrew = False

SPIKE_SHOT = Trait(
    "Spike Shot",
    "As an action, this unit forces a target unit to succeed on a DC 12 Power test or suffer 2 casualties and become weakened. An affected unit can repeat this power test at the end of each of its activations to lose the weakened unit condition. Recharge 5–6.",
).homebrew = False

SPLIT = Trait(
    "Split",
    "When this unit is diminished, place an identical unit with the same current battle statistics and casualties in an empty adjacent space.",
).homebrew = False

SPORES = Trait(
    "Spores",
    "When this unit is targeted by a successful Attack test from an infantry, cavalry, or aerial unit, the attacking unit must succeed on a DC 13 Power test or become disoriented.",
).homebrew = False

STALWART = Trait(
    "Stalwart",
    "While this unit is diminished, opposed infantry and cavalry units have disadvantage on Power tests against it.",
).homebrew = False

STINKY = Trait(
    "Stinky",
    "Any opposed unit adjacent to this unit has disadvantage on Attack tests.",
).homebrew = False

STONE = Trait(
    "Stone",
    "Each opposed unit that activates adjacent to this unit suffers 1 casualty.",
).homebrew = False

STONESKIN = Trait(
    "Stoneskin",
    "As a reaction to suffering 1 or more casualties from any opposed artillery unit, this unit can ignore 1 of those casualties.",
).homebrew = False

STRENGTH_IN_NUMBERS = Trait(
    "Strength in Numbers",
    "This unit begins the battle with 1 additional casualty for each other undead unit in its army (up to a maximum of 12 casualties).",
).homebrew = False

STUPID = Trait(
    "Stupid",
    "Each time it attacks, this unit has a 25 percent chance of ignoring its intended target and attacking a random adjacent unit.",
).homebrew = False

SWORDS_OF_THE_DRAGON_LORD = Trait(
    "Swords of the Dragon Lord",
    "When this unit makes a successful Attack test against a target unit, the target must succeed on a DC 13 Morale test or suffer 1 additional casualty.",
).homebrew = False

TO_THE_DEATH = Trait(
    "To the Death",
    "If this unit breaks as a result of an opposed infantry, cavalry, or aerial unit’s Attack or Power test, the attacking unit suffers 1 casualty.",
).homebrew = False

VETERANS_OF_A_THOUSAND_WARS = Trait(
    "Veterans of a Thousand Wars",
    "This unit’s movement increases by 1. When attacking units of a lower tier, its damage increases by 1.",
).homebrew = False

WAIL = Trait(
    "Wail",
    "Once per battle, this unit can use an action to force each adjacent opposed unit to make a DC 15 Power test. On a failure, a unit suffers 1 casualty, and its Morale bonus is reduced to 0 until the end of its next activation. On a success, a unit has disadvantage on Morale tests until the end of its next activation.",
).homebrew = False

WARBRED = Trait(
    "Warbred",
    "As a reaction to succeeding on a Power test as part of an attack, this unit can make a DC 10 Command test. On a success, this unit can attack again.",
).homebrew = False

WAVE = Trait(
    "Wave",
    "When this unit succeeds on a Power test as part of an attack against an opposed unit, the opposed unit is pushed back 1 space if there is an empty space behind it. If there is no empty space, the opposed unit and the unit behind it each suffer 1 casualty.",
).homebrew = False

WHIRLWIND = Trait(
    "Whirlwind",
    "When this unit succeeds on an Attack test against an opposed infantry unit, that unit takes −2 to Attack and Defense. Each opposed unit can be affected by this trait once per battle.",
).homebrew = False

YOU_FOLLOW = Trait(
    "You Follow!",
    "Whenever this unit successfully uses the Follow Up maneuver, each goblinoid unit in the rank this unit leaves can move 1 space.",
).homebrew = False
