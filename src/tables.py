'''
Created on Dec 1, 2014

@author: Disley
'''

common_curiosity = {1 : "Ostracised from the community, more than happy to help ruin the plans of others for good or bad",
                    2 : "Were once caught in a compromising position with a well-bred member of large livestock. It brings everyone else great joy to ensure they never live it down.",
                    3 : "Have a surprisingly large assortment of goods for trade or sale.",
                    4 : "Incredibly friendly, attempting to summon an earth-shaking terror using an underground shrine they found, need help recovering the innocuous missing pieces.",
                    5 : "Fervent devotees to a known religion.",
                    6 : "Protectors of an ancient and terrible secret.",
                    7 : "Cannibals.",
                    8 : "Members of the same bloodline.",
                    9 : "Addicted to a strange and wonderful new drug they have discovered.",
                    10: """Under the influence of a sentient plant growing in the area, its form depends on the number of homes affected:
                            1-2 Discoloured patches on the skin, small hidden sprouts.
                            3-5 Root clusters in the darkness at the back of their throats, speaking for them, a fledgling mother plant beginning to grow in the area.
                            6+ A large, established plant, protected by those given over more wholly to its symbiosis.
                        """,
                    11: "Insect cult. If six or more homes are affected, a shrine containing a physical manifestation of their worship exists in the area.",
                    12: "Aggressive/distrustful towards outsiders.",
                    13: "Dress like demons and prance around burning pyres when the moon is full.",
                    14: "Militant nudists.",
                    15: "Share a psychic connection to one another that allows them to simultaneously experience everything that happens to each individual member, and grants them terrifying powers of the mind when their number exceeds fourteen.",
                    16: "Extremely welcoming towards outsiders.",
                    17: "Enthusiastic practitioners of a strange pastime.",
                    18: "Speak in a dialect not used for centuries.",
                    19: "Organic body-horror replacements from a fallen star in the hills. They smell of thyme and their flesh is all-too pliable.",
                    20: "Will attempt to burn Magic-Users and Clerics like witches.",
                    21: "Capture children of all ages as offering to the toad beast in the woods for the protection of the town. The sacrifices sleep curled within amber pus-filled holes in the hardened skin of its belly until they emerge as misshapen and fantastic children of the fae. The rest of the town is oblivious.",
                    22: "Their windows are dark and they do not answer their doors.",
                    23: "Share a competitive rivalry over something quaint: (Hunting, baking, growing large vegetables, needlework, gardening, offering sacrifices to their abhorrent god, etc.)",
                    24: "Are afflicted by a terrible, undocumented ailment.",
                    25: "Wash their dead in the creek and bury them beneath the silt, returning in a week's time to retrieve their bare, yellowed bones.",
                    26: "Form the militia of the Blue Palm, adept in the use of paralytic poisons derived from local flowers.",
                    27: "Incredibly eager to marry-off/apprentice their sons and daughters, will go to great lengths to prove the superiority of their children over their neighbour's.",
                    28: "Summoned a melting pyramid-headed lady of unspeakable lust and terror as a plaything and instead became her emotional puppets. She can't hurt them but is trying damned hard to make them hurt themselves, she can't leave this plane of existence until they are all dead. She resides in secret at the home nearest to the centre of the group and she hates it here.",
                    29: "Esoteric horticultural society, with a 3 in 6 chance of having access to any rare plant you care to mention and a high likelihood of losing their minds over any specimens of your own you'd like to share.",
                    30: "Recently welcomed the offspring of their god into the womb of a blushing bride on her wedding night, we're all terribly proud."
                    }
                    
significant_features = {1: {1 : "A partly-excavated ziggurat hewn from seemingly moist red stone.",
                            2 : "A shunned manor.",
                            3 : "Large statue of a many-armed woman dangling various iron scales from chains. A golden swine stands in one of the largest, holes in its back collect rainwater that drains slowly from its teats over time. Various wedding rites and legal proceedings are conducted by filling the other scales then climbing into the final scale to release the lever protruding from the statue's mouth to discover if they match the weight of the swine.",
                            4 : "A series of bronze columns wrapped in thick, healthy vines, bearing forth sprays of waxy leaves and plump purple fruits."},
                        2: {1 : "An obscenely elaborate gateway to nowhere.",
                            2 : "A well-equipped timber fort, with the severed heads of horses impaled on pikes at intervals around its perimeter.",
                            3 : "A strange sinkhole rife with brilliantly-coloured fungus.",
                            4 : """Monolith of carven white soapstone in the centre of town. Rearrange the houses so that they form rough curving lines radiating out from the monolith.",
                                Most of the townspeople seem entirely unaware of this pattern, but once you mention it to them will descend into obsession over it, eventually seeking to unlock the monolith and what lies beneath.
                                """},
                        3: {1 : "Clusters of huge pink-tinged crystals growing from some obscured central mass.",
                            2 : "Memorial crypt holding the fallen of past battles, decorated above by the bones of their enemies.",
                            3 : "Bridge over an algae-strewn stream, drilled full of holes. It is a rite of passage for the young men, not for pleasure, but to deny the begging crone of the water their manhood while she gnaws at their thighs.",
                            4 : "Elaborate tower like one big perpetual motion water mechanism built around a seemingly bottomless pool full of golden eels."},
                        4: {1 : "Many-spired black stone church casting a cryptic shadow.",
                            2 : "A mostly-ransacked library and observatory converted into a watchtower.",
                            3 : "An enormous pale tree, its reaching branches dropping soft purple leaves over the town. Lost baby teeth have been hammered into its twisting trunk, gradually sucked in over the years, and a dark hole gapes near its swollen roots, the faint soft sound of moving air.",
                            4 : "An alchemist's pit of living molten metal contained below a ring of standing stones and a descending spiral staircase."}}

features_of_interest = {1 : "Weather-worn image of an old god.",
                        2 : "Mystically placed patterns of stones.",
                        3 : "Evidence of some recent natural disturbance.",
                        4 : "Hanging tree.",
                        5 : "Sour earth.",
                        6 : "Verdant hole in the earth.",
                        7 : "Watchtower.",
                        8 : "Healer's hut.",
                        9 : "Remains of destroyed structure.",
                        10: "Site of recent slaughter.",
                        11: "Patch of stubborn forest.",
                        12: "Wellspring."}

whos_in_charge = {1 : "The nearest odd number to the d4.",
                  2 : "The nearest even number to the d4.",
                  3 : "The nearest matching number to the d4.",
                  4 : "The furthest matching number from the d4.",
                  5 : "The furthest odd number from the d4.",
                  6 : "The furthest even number from the d4.",
                  7 : "Council with a representative from each number group lower than the d4.",
                  8 : "Council with a representative from each number group.",
                  9 : "Council with a representative from each number group higher than the d4.",
                  10: "We do not speak its name."}

relationships = {1 : "Irrational dislike.",
                 2 : "Firm friends.",
                 3 : "Harbours terrible suspicion.",
                 4 : "Owes a debt.",
                 5 : "Adultery.",
                 6 : "Long family history.",
                 7 : "Business.",
                 8 : "Blackmail.",
                 9 : "Estranged friends/lovers.",
                 10: "Political undertones.",
                 11: "Blatant fear.",
                 12: "Yearning.",
                 13: "Vast respect.",
                 14: "Black magic.",
                 15: "Rivalry.",
                 16: "Knows varied secrets.",
                 17: "Distrust.",
                 18: "Mockery.",
                 19: "Betrayal.",
                 20: "Blood feud."}