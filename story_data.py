# Complete Story Data for "Consider the Consequences" (1930)
# All 83 segments with choices and branching paths

STORY_DATA = {
    # HELEN'S STORY (35 segments)
    "H-START": {
        "character": "Helen",
        "text": """You are HELEN, a young woman facing a pivotal choice in your life.

Two men want to marry you:
- JED: Charming, passionate, wealthy heir - but troubled and unreliable
- SAUNDERS: Steady, responsible, practical businessman - but less exciting

Your choice will determine your entire future...""",
        "choices": [
            {"text": "Begin Helen's story", "goto": "H-1"}
        ]
    },

    "H-1": {
        "character": "Helen",
        "text": """Helen Rogers,20, with honey-gold hair and gray-green eyes, is madly in love with Jed Harringdale. Her parents oppose the marriage - Jed never settled down to work, his health is poor, he drinks and lives recklessly. Helen's family wants her to marry Saunders Mead instead (prudent, hard-working, devoted but unromantic).

Should Helen marry Jed against her parents' advice?""",
        "choices": [
            {"text": "Defy parents and stay with Jed", "goto": "H-2"},
            {"text": "Choose prudence and break with Jed", "goto": "H-3"}
        ]
    },

    "H-2": {
        "character": "Helen",
        "text": """Helen refuses to break her engagement. Jed proposes eloping to New York State for immediate marriage.""",
        "choices": [
            {"text": "Elope with Jed", "goto": "H-4"},
            {"text": "Return home to face opposition", "goto": "H-5"}
        ]
    },

    "H-3": {
        "character": "Helen",
        "text": """Helen breaks with Jed. She's miserable and wants to escape to New York where friend Marian Cole has found her a job. Her parents oppose - mother is dependent, brother Simeon going to South America. They ask her to stay 2 years.""",
        "choices": [
            {"text": "Stay home in Franklin", "goto": "H-6"},
            {"text": "Leave for New York", "goto": "H-7"}
        ]
    },

    "H-4": {
        "character": "Helen",
        "text": """Perfect honeymoon! Helen and Jed return to Franklin. Mrs. Harringdale invites them to live with her but refuses other help.""",
        "choices": [
            {"text": "Accept living with Mrs. Harringdale", "goto": "H-8"},
            {"text": "Refuse and find own place", "goto": "H-9"}
        ]
    },

    "H-5": {
        "character": "Helen",
        "text": """Jed can't stand up to his mother. After a year, he begs Helen to wait another year. Then Jed releases Helen from all promises - his mother's health prevents marriage.""",
        "choices": [
            {"text": "Stick by Jed and wait", "goto": "H-10"},
            {"text": "Break engagement completely", "goto": "H-11"}
        ]
    },

    "H-6": {
        "character": "Helen",
        "text": """2 years pass. Simeon home for 3 months then to Alaska. Mother semi-invalid. Two job offers:
- Franklin: $12/week stenography, can live at home
- New York (Marian): $20/week, chance for promotion""",
        "choices": [
            {"text": "Take Franklin job", "goto": "H-12"},
            {"text": "Take New York job", "goto": "H-13"}
        ]
    },

    "H-7": {
        "character": "Helen",
        "text": """Gets low-pay copy-holder job at printing plant. Works up to switchboard, then becomes important in office. 2 years later, Marian offers her $50/week magazine job. Boss desperately needs her.""",
        "choices": [
            {"text": "Stay at printing plant", "goto": "H-14"},
            {"text": "Take magazine job", "goto": "H-13"}
        ]
    },

    "H-8": {
        "character": "Helen",
        "text": """Constant tension between Helen and mother-in-law over Jed. Jed escapes to club (drinking, gambling). Baby born - brief armistice, then worse. Jed refuses to leave mother's home. Jed dies suddenly. Helen dependent on Mrs. Harringdale who gives home but refuses separate maintenance.""",
        "choices": [
            {"text": "Stay with Mrs. Harringdale for child's inheritance", "goto": "H-15"},
            {"text": "Leave and earn own living", "goto": "H-17"}
        ]
    },

    "H-9": {
        "character": "Helen",
        "text": """Jed can't handle hardship. Baby increases expenses. Mrs. Harringdale refuses aid. Jed returns to drinking, loses job, becomes auto salesman. Serious accident while drunk. Mrs. Harringdale helps but too late - Jed dies. Offers to adopt child if Helen relinquishes legal claim.""",
        "choices": [
            {"text": "Give up child to Mrs. Harringdale", "goto": "H-16"},
            {"text": "Keep child despite poverty", "goto": "H-17"}
        ]
    },

    "H-10": {
        "character": "Helen",
        "text": """Mrs. Harringdale takes Jed on trips for his health. Helen waits and waits. Mrs. Harringdale finally dies when Helen is 46, Jed almost 50. They marry but Jed is a confirmed invalid. Helen has a delightful old age but lost 25 years of life.""",
        "ending": "You waited for love, but at what cost? Twenty-five years lost waiting for a future that would never fully arrive."
    },

    "H-11": {
        "character": "Helen",
        "text": """Marian telegraphs about New York job. Mother semi-invalid, wants Helen to stay in Franklin for lower salary.""",
        "choices": [
            {"text": "Stay in Franklin", "goto": "H-12"},
            {"text": "Go to New York", "goto": "H-13"}
        ]
    },

    "H-12": {
        "character": "Helen",
        "text": """Salary raised to $18. Working hard at office and home. Father dies, Helen has nervous collapse, uses savings. Saunders Mead begs her to marry him. Brother Simeon offers to support mother and Helen if she stays home.""",
        "choices": [
            {"text": "Marry Saunders", "goto": "H-18"},
            {"text": "Accept Simeon's support offer", "goto": "H-19"}
        ]
    },

    "H-13": {
        "character": "Helen",
        "text": """Lives with Marian in Greenwich Village studio. Gay social life. 5pm emergency: editor needs her to work overtime to fix libelous article. Important party that night with new dress for Phil Burns (young artist).""",
        "choices": [
            {"text": "Go to the party", "goto": "H-20"},
            {"text": "Work overtime", "goto": "H-21"}
        ]
    },

    "H-14": {
        "character": "Helen",
        "text": """Can't afford extravagances of Marian's crowd. Misses buying Chinese-red dress for party with Phil Burns. Interest centers on printing business and employer's appreciation. Vacations with widowed mother. Receives marriage proposals but not interested.""",
        "ending": "A safe, uneventful life. No failures, no triumphs. Security without passion."
    },

    "H-15": {
        "character": "Helen",
        "text": """Like nursery governess, not mother. Grandmother has power and money, gives child all treats. Helen has no clothes, money, or liberty. Mrs. Harringdale dies after 20 years. Young Jed goes abroad, marries, sends allowance but rarely visits. Helen plays bridge, does civic work.""",
        "ending": "Safe but never lived joyously except for the honeymoon. You sacrificed freedom for security that proved hollow."
    },

    "H-16": {
        "character": "Helen",
        "text": """Lives with widowed invalid mother. Obsessed with getting child back. Courts return child but he's spoiled and resents correction, chooses grandmother. As adult, son makes allowance but rarely visits. Helen drifts into invalidism.""",
        "ending": "You lost everything except tragedy. The child you gave up never truly became yours again."
    },

    "H-17": {
        "character": "Helen",
        "text": """Takes business course, gets secretary job $20/week. Boarding house landlady watches child during work. Exhausted, worried. Saunders Mead asks her to marry him again.""",
        "choices": [
            {"text": "Marry Saunders", "goto": "H-22"},
            {"text": "Refuse Saunders, continue alone", "goto": "H-23"}
        ]
    },

    "H-18": {
        "character": "Helen",
        "text": """Happy marriage! New house on Western Boulevard. Babies, servants, social life. Bridge, golf, garden club. Papers published in Franklin News. President of Missionary Society. Saunders very proud of wife.""",
        "ending": "A successful, sensible life. You chose security and found genuine happiness in a stable partnership."
    },

    "H-19": {
        "character": "Helen",
        "text": """Paradise at first not working. Mother encourages social life but Helen doesn't fit young married set. Church work. At 35, missionary Mr. Montgomery (widower, 5 children) offers marriage and China. Mother aghast, Simeon cables disapproval, Franklin takes sides.""",
        "choices": [
            {"text": "Go to China with Montgomery", "goto": "H-24"},
            {"text": "Stay with mother", "goto": "H-25"}
        ]
    },

    "H-20": {
        "character": "Helen",
        "text": """Chinese-red dress successful! All men notice. Phil Burns (artist) proposes after a week, marry at Little Church around the Corner. Helen keeps job, postpones babies. Gives enough attention to job to avoid being fired, rest to husband.""",
        "ending": "Marriage is a success, though you're not a great employee. Love triumphed over ambition."
    },

    "H-21": {
        "character": "Helen",
        "text": """Works seriously, impresses editor Paul Merritt. Rises rapidly - voice in policy, handles famous authors, trips to Europe. Paul is married but unhappy - wife wants him in real estate, nags about money. Paul and Helen fall in love. Paul wants divorce.""",
        "choices": [
            {"text": "Give up Paul completely", "goto": "H-26"},
            {"text": "Encourage his divorce", "goto": "H-27"},
            {"text": "Be lovers while he stays married", "goto": "H-28"}
        ]
    },

    "H-22": {
        "character": "Helen",
        "text": """Married one year, two years since Jed died. Helen talks constantly about Jed to child. Child healthy, devoted to stepfather. Saunders plans trip to city for dinner/theater on 2nd anniversary of Jed's death. Helen planned to visit Jed's grave.""",
        "choices": [
            {"text": "Go with Saunders on the trip", "goto": "H-29"},
            {"text": "Visit Jed's grave instead", "goto": "H-30"}
        ]
    },

    "H-23": {
        "character": "Helen",
        "text": """Tired, shabby, overworked but struggles bravely. Young Jed protective, refuses college from grandmother to work. Grandmother leaves money to church memorial. Jed works for Saunders Mead's store, develops merchandising genius. By 21 makes Paris trips. By 30, Saunders retires, gives management to Jed.""",
        "ending": "Your courage was rewarded with your son's love, respect, and success. Independence brought dignity."
    },

    "H-24": {
        "character": "Helen",
        "text": """Guilt about lonely mother, but too busy with 5 stepchildren, 2 own children, mission work, attached husband. Sends diary letters, Franklin missionary society meets in mother's room to hear them, publishes book widely circulated.""",
        "ending": "People who said you should stay now say 'How fortunate you are in your daughter!' Adventure rewarded."
    },

    "H-25": {
        "character": "Helen",
        "text": """Quiet 15 years. Simeon marries, lives in New York. Small trips. Mother dies when Helen is 50. Simeon stops supporting her, she must work. Takes boarders in old house.""",
        "ending": "A life of self-abnegation. Everyone praises and pities you. Duty brought respect but not fulfillment."
    },

    "H-26": {
        "character": "Helen",
        "text": """Quits job. Nat Hebling (author she discovered) finds her publishing job. Love for Paul turns to Nat (blond, lanky, temperamental). Marries Nat. Circle of artistic people, takes up short-story writing.""",
        "ending": "Life as wife, mother, woman of affairs works harmoniously. You can love a second time as heartily as the first."
    },

    "H-27": {
        "character": "Helen",
        "text": """Ghastly year. Wife finally agrees for large alimony. Helen and Paul marry, desperately poor despite both working. Can't have children. Strain of Paul visiting former family often. Accept poverty as price for each other.""",
        "ending": "Helen plans to save for year off to have baby. Love came at a high cost, but you chose it anyway."
    },

    "H-28": {
        "character": "Helen",
        "text": """Helen takes own apartment. Several moves due to landlord problems. Emotionally reacts old-fashioned way despite intellectual attitude. Jealous of wife and children. Wild desire for own child.""",
        "choices": [
            {"text": "Have a child out of wedlock", "goto": "H-31"},
            {"text": "Don't have a child", "goto": "H-32"}
        ]
    },

    "H-29": {
        "character": "Helen",
        "text": """Takes off black dress without mentioning anniversary. Beautiful ride, meets Carol getting divorce. Came back closer to Saunders than ever, convinced having good time is wife's duty.""",
        "ending": "You chose the living over the dead. The marriage became genuinely happy."
    },

    "H-30": {
        "character": "Helen",
        "text": """Sweet sadness with boy at grave. Saunders stops inviting her on trips. Telegram for Saunders from C. Lane: 'Telegraph five hundred dollars more at once.' Saunders lending Carol money for divorce. Admits unfaithfulness, says justified since Helen doesn't love him.""",
        "choices": [
            {"text": "Divorce Saunders", "goto": "H-33"},
            {"text": "Don't divorce Saunders", "goto": "H-34"}
        ]
    },

    "H-31": {
        "character": "Helen",
        "text": """Friends stand by but tabloids find story. 'Eugenic baby' scandal. Paul's name revealed, photos, interviews with wife and 4 children. Lush sentimentality worse than condemnation. Story rehashed whenever Helen or Paul do good work.""",
        "ending": "Passing humiliation and permanent record. Freedom came at the cost of scandal."
    },

    "H-32": {
        "character": "Helen",
        "text": """Love doesn't crash on society's disapproval but conflict too much for Paul - nervous breakdown, sanatorium. Helen gets publishing job through Nat Hebling. Lonely after separation from Paul. After 2 years marries Nat.""",
        "ending": "Life with Paul taught her to handle temperamental man and appreciate conventional domesticity. Settled into conventional marriage."
    },

    "H-33": {
        "character": "Helen",
        "text": """Saunders's unfaithfulness unbearable. Accepts alimony for boy. Independent with child, freedom, income but lost ideals. Searches for distraction at resorts. Meets and marries tremendously wealthy man.""",
        "ending": "Carries discontent into splendid life. Has material benefits, lacks love and generosity."
    },

    "H-34": {
        "character": "Helen",
        "text": """Marriage not pleasant without love. Neither party doing any loving. Saunders plans skiing weekend. Young Jed (8-10 years old) becomes hysterical: 'Oh, don't go, Mummie!'""",
        "choices": [
            {"text": "Stay with child", "goto": "H-35"},
            {"text": "Go with husband", "goto": "H-36"}
        ]
    },

    "H-35": {
        "character": "Helen",
        "text": """Passionate preoccupation with child too intense for husband interest. Live under same roof, separate ways. Saunders physically comfortable though disappointed. Helen lives whole life in son. Young Jed leaves home early but never escapes her warnings.""",
        "ending": "The child alternately dependent and antagonistic. You smothered what you loved most."
    },

    "H-36": {
        "character": "Helen",
        "text": """Chance to correct mistake. Tries to please Saunders, finds she's loving him differently than Jed. Home harmonious, Saunders responds to affection. More children.""",
        "ending": "Not romance of girlhood but satisfactory working partnership. A happy wife and mother at last."
    },

    # JED'S STORY (18 segments)
    "J-START": {
        "character": "Jed",
        "text": """You are JED, the only son of rich widow Mrs. Harringdale.

You're charming and wealthy but spoiled - no discipline, not healthy/wise. Returns from Harvard in racing car 'Scarlet Siren.' Meet Gwen Murphy at Whoopee-Land with friend Saunders Mead.

Passionate summer love affair with working-class Gwen. Now she tells you she's pregnant and you must marry. Mrs. Harringdale offers Gwen money to release you, accuses her of trapping you.

Your story involves romance, responsibility, and the weight of family expectations...""",
        "choices": [
            {"text": "Begin Jed's story", "goto": "J-1"}
        ]
    },

    "J-1": {
        "character": "Jed",
        "text": """Should you marry Gwen Murphy who is pregnant with your child?""",
        "choices": [
            {"text": "Marry Gwen", "goto": "J-2"},
            {"text": "Don't marry Gwen", "goto": "J-3"}
        ]
    },

    "J-2": {
        "character": "Jed",
        "text": """Happy first weeks. Live with Mr. Murphy (iceman). Baby comes - saves situation briefly. Jed can't make home for them. Mr. Murphy and Jed don't get along. Gwen amazed educated man can't hold job. Women take matters in hand - Gwen gets alimony, moves to own house with baby.

Jed broods over failure. Doctors advise European trip alone. Takes up sketching in Switzerland, art school in Paris, becomes promising student. Mother writes: family lawyer died, come home to manage estate.""",
        "choices": [
            {"text": "Return to Franklin to manage estate", "goto": "J-4"},
            {"text": "Stay in Paris to pursue art", "goto": "J-5"}
        ]
    },

    "J-3": {
        "character": "Jed",
        "text": """Returns to college feeling dissatisfied. Gwen goes to New York, child born and adopted by wealthy Joralemonsons. Jed drinks to escape guilt, fails mid-years, dropped from college. Mother glad to have him home.

Mrs. Harringdale arranges Easter house-party with Carol Lane (pretty, gay New York girl, summers in Franklin). Jed falls in love, engagement announced. Tells Carol about Gwen. Carol tells him she also had pre-marital intimacy last summer.""",
        "choices": [
            {"text": "Go on with marriage to Carol", "goto": "J-6"},
            {"text": "Break engagement with Carol", "goto": "J-7"}
        ]
    },

    "J-4": {
        "character": "Jed",
        "text": """Happy first weeks. Studio in attic costs more than expected but has mother's money control. Invests in undeveloped real estate. Income decreases, both spend freely. Sells bonds, buys conservative stocks - they pass dividends. Sells at loss, tries speculation - loses more.

Persuaded to invest in local manufacturing as vice-president. Business does well initially. Rebuilds family home beautifully. Orders fall off, plant idle. Mortgages real estate. Patent-infringement suit lost - must pay back royalties. Mother nags constantly. Creditor threatens bankruptcy.

Jed returns to factory at night to face insolvency. Contemplates suicide. Lights cigarette, throws match in waste basket, flames up. Thinks of $100,000 insurance. Walks out as watchman sees him. Fire destroys plant. Watchman tells story. Jed faces arrest for arson. Picks up revolver as police ring bell.""",
        "choices": [
            {"text": "Commit suicide", "goto": "J-8"},
            {"text": "Live on disgraced", "goto": "J-9"}
        ]
    },

    "J-5": {
        "character": "Jed",
        "text": """Works hard to justify refusing mother. Gains recognition. Alpine landscape hung in Salon. Plans European glacier series. Visits mother first. Stops in New York, renews acquaintance with Marian Cole (Franklin girl, now secretary with big opportunities).

Deeply in love with Marian. Proposes. She loves him but won't give up career unless he makes New York headquarters. Won't marry man too crystallized to adapt to wife with career.""",
        "choices": [
            {"text": "Marry Marian, move to New York", "goto": "J-10"},
            {"text": "Give up Marian, stay in Paris", "goto": "J-11"}
        ]
    },

    "J-6": {
        "character": "Jed",
        "text": """Mrs. Harringdale builds doll's house on estate. Carol wants 2 years abroad first. Traveling delights Jed. Mediterranean yachting cruise as guests of Price Bullen and young French wife Vauncey. Jed falls genuinely, deeply, maturely in love with Vauncey. She refuses affair despite unhappy marriage.

Concert evening at Antibes hotel. Carol decides not to go. Jed and Vauncey talk on rocks - she admits love but won't leave husband. Jed goes to café to drink. Drunk, decides to confront Bullen about divorce for Vauncey. Hears Carol's laugh from Bullen's bedroom. Attacks Bullen with bottle. Bullen dies. Carol wipes bottle, hurries Jed to room. Her alibi keeps suspicion from Jed.""",
        "choices": [
            {"text": "Give himself up for murder", "goto": "J-12"},
            {"text": "Stay silent", "goto": "J-13"}
        ]
    },

    "J-7": {
        "character": "Jed",
        "text": """Next love affair (year later) with Helen Rogers - handsome, grave blond girl, more restful than Carol. Mrs. Harringdale opposes (no money or social prominence like Carol). Wants elopement but Helen insists on open marriage.

Two distressing years. Mrs. Harringdale develops high blood pressure. Doctors warn excitement could cause fatal stroke. After 2 years Helen demands separate or marry. Jed must choose between mother's health and Helen.""",
        "choices": [
            {"text": "Marry Helen despite mother", "goto": "J-14"},
            {"text": "Stand by mother, give up Helen", "goto": "J-15"}
        ]
    },

    "J-8": {
        "character": "Jed",
        "text": """Insolvency and death affect mother, former wife Gwen, and daughter. Gwen and child live with Mr. Murphy, she gets job at Saunders Mead's store. Mrs. Harringdale's property sale gives enough to skimp along in cheap boarding houses. Always difficult, now worse having lost only person she loved.""",
        "ending": "Your amiable method of letting others decide dragged others down with you. Suicide solved nothing."
    },

    "J-9": {
        "character": "Jed",
        "text": """Trial short, evidence plain, pleads guilty. Convicted of arson, long sentence but serves only few years. Confinement and worry break health. Before death in prison hospital, mother visits frequently, renew tender early relations.""",
        "ending": "Comfort to unhappy mother makes you glad you resisted suicide. You spared mother grief of feeling responsible for son's death."
    },

    "J-10": {
        "character": "Jed",
        "text": """Doesn't hold grudge. Wonderful Canadian honeymoon. Discovers Columbia Ice Field - paints tremendously successful picture, beginning of famous Canadian glacier series. Success keeps him from being overshadowed by beautiful vital wife. She makes business name, runs charming home, has 3 babies. Makes friends with his mother, persuades first wife Gwen to allow daughter Madeleine to visit.""",
        "ending": "Wife with unusual combination of masculine independence and feminine tenderness guides you to make most of yourself. Success and love achieved."
    },

    "J-11": {
        "character": "Jed",
        "text": """Grows goatee, looks Parisian. Marries French Huguenot family - likes deferential attitude better than American independence. Part of French family life. Escapes to discreet affairs without social condemnation. Good work, completes European glacier series.""",
        "ending": "Gave up Marian for work - has work but not Marian. Being more adaptable might have had both."
    },

    "J-12": {
        "character": "Jed",
        "text": """Tells lawyer whole story. Lawyer says French jury lenient on man killing wife's lover under unwritten law. Unless pleads this, faces long sentence. Consults Carol who begs him not to tell, sure he'll get off.""",
        "choices": [
            {"text": "Tell truth about finding wife with Bullen (unwritten law)", "goto": "J-16"},
            {"text": "Protect wife's reputation", "goto": "J-17"}
        ]
    },

    "J-13": {
        "character": "Jed",
        "text": """Police investigations come to nothing - no motive found. Assumption: Bullen surprised thief from balcony. Jed feels watched after leaving Antibes. Carol and Jed completely alienated but pretend united life. Dare not divorce lest scandal revealed. Vauncey drops out. Return to Franklin. Make home with Mrs. Harringdale. After few years, separate trips.""",
        "ending": "Cloud over you not so bad. Family life not unhappy when together - appreciate Mrs. Harringdale's unconscious protection since you're not all to each other."
    },

    "J-14": {
        "character": "Jed",
        "text": """Two hours late to wedding because mother in state. During ceremony, mother has stroke - loses speech and motion. Wedding trip postponed 6 years. Live at Mrs. Harringdale's, invalid with 2 nurses but demands constant attention from Jed. Eventually dies. Family travels, years in France, Jed sketches.""",
        "ending": "Helen realizes he's not businessman, persuades him to let lawyers handle estate, he paints (unusual talent). Disobeying irrational mother made everybody except mother moderately happy."
    },

    "J-15": {
        "character": "Jed",
        "text": """Decision admirable or simply inability to decide. While saying 'I'll wait and see,' Helen leaves for city job. Break improves mother's disposition. Three love-affairs gone wrong but doesn't discourage trying others, each briefer. Older generation calls him Don Juan with disapproval.""",
        "ending": "Tragedy of eternal quest for perfect woman to satisfy both mother and yourself. Perfect son, no good as husband."
    },

    "J-16": {
        "character": "Jed",
        "text": """Carol practical - when necessary to save Jed, represents Bullen as friend who took advantage of innocence. Trial enjoyed by press of two countries. Acquitted on unwritten law. Carol stands by through trial, sues for divorce afterward. Returns to Franklin but cloud cuts him from friends. Lives as recluse, absorbed in solitary interests.

Trip abroad with mother, meets Joralemonsons and daughter Anne (his adopted daughter from Gwen). Gets acquainted - extraordinarily congenial. Anne confides she's adopted, longs to know parents. Jed faces whether to tell.""",
        "choices": [
            {"text": "Tell Anne he's her father", "goto": "J-18"},
            {"text": "Don't tell Anne", "goto": "J-19"}
        ]
    },

    "J-17": {
        "character": "Jed",
        "text": """Public assumes Jed murdered Bullen because in love with Bullen's wife Vauncey. Lawyer says jury won't be lenient toward one who murdered mistress's husband. Acquitted. Carol divorces immediately, later marries English officer.

Vauncey horrified at Carol's desertion. Won't abandon Jed, feels life bound in common expiation. Religion forbids marrying Jed but finds consolation having him near. Returns to parents' chateau in southern France. Jed settles in villa 3 miles away. Once weekly received for dinner, play backgammon. Routine continues after parents' death.""",
        "ending": "Long placid life measured by evening chimes. Not unhappy - found perfect woman (one you couldn't have). Dignity in catastrophe from foolish misspent youth."
    },

    "J-18": {
        "character": "Jed",
        "text": """Unprepared for tumult in unsophisticated girl. Dreamed of father overwhelmed by misfortune, not involved in notorious murder. Learns he deserted mother, allowed child born with illegitimacy stigma. Can't understand woman stronger than man. Sees mother seduced, herself outcast through pusillanimity.

Takes story to foster-parents, never so dear. Mr. Joralemon enraged. Jed realizes what he'd done. Looking back sees futile life despite good intentions. Next morning missing, cabin not slept in. Threw himself from ship during night.""",
        "ending": "Left broken mother alone, daughter who'd never forget she sent unloved father to death. Last time did wrong thing."
    },

    "J-19": {
        "character": "Jed",
        "text": """First time knew love making another's happiness more important than own. Lovely girl dearer than mother, Gwen, Carol, or Vauncey. Sense of fatherhood awakened late gave strength to put aside selfish desire. When she confided day-dreams about unknown parents, saving her from knowledge of illegitimacy and worthless father gave new self-respect.""",
        "ending": "Now indeed felt father, protecting from shock even at expense of own satisfaction. Some depression left him, released energy focused on painting. Had work now, found congenial friends through it."
    },

    # SAUNDERS' STORY (30 segments)
    "S-START": {
        "character": "Saunders",
        "text": """You are SAUNDERS, raised in pleasant white frame house in Franklin.

Father is postmaster, small income but never felt poor. Eldest child, developed responsibility early. Graduated high school, got job at Franklin Dry Goods Store. Father's death made you family head.

Old Mr. Braley (store owner) offers chance to invest your $500 and gradually buy controlling interest. But younger brother Alfred wants to go to Massachusetts Tech for architecture. Has saved $100. If borrows your $500, can scrape through first year.

Your choices will define what kind of leader and man you become...""",
        "choices": [
            {"text": "Begin Saunders' story", "goto": "S-1"}
        ]
    },

    "S-1": {
        "character": "Saunders",
        "text": """Should you lend $500 to Alfred for college, or invest in the store?""",
        "choices": [
            {"text": "Lend money to Alfred", "goto": "S-2"},
            {"text": "Invest in store", "goto": "S-3"}
        ]
    },

    "S-2": {
        "character": "Saunders",
        "text": """Gives $500 without complaining. Alfred does brilliantly. Alfred's senior year thesis: grammar-school design for Franklin. Alderman Donovan calls - Board virtually decided to use Alfred's plans. Offers $10,000 for Mead property (generous not excessive).

But beneath words: Saunders must pay $2,000 in bills (not check) directly to Board president. This is graft. If accepts: Alfred's design accepted, family gets modern house. If refuses: Alfred's chance lost.""",
        "choices": [
            {"text": "Accept the graft offer", "goto": "S-4"},
            {"text": "Refuse graft", "goto": "S-5"}
        ]
    },

    "S-3": {
        "character": "Saunders",
        "text": """Alfred disappointed. Business outlook cheerful but home unpleasant. Saunders gets Alfred job at store when opening comes. Alfred makes wretched clerk. Great-uncle dies unexpectedly, leaves $500 to each Mead. Alfred radiantly goes to Tech.

Saunders unsure what to do with $500. Young only once - could spend windfall on second-hand car. But risks standing with Mr. Braley. Wants to be millionaire - first $10,000 is hardest.""",
        "choices": [
            {"text": "Buy a car", "goto": "S-6"},
            {"text": "Invest windfall in store", "goto": "S-7"}
        ]
    },

    "S-4": {
        "character": "Saunders",
        "text": """Excavation finished, foundation begun. Alfred becomes glum. Lengthy conferences with aldermen. Saunders realizes what temptation he's put Alfred in. Asks Alfred frankly about graft. Whole thing comes out. Aldermen substituted inferior plans - $100,000 appropriation for $60,000 actual cost. $40,000 split among ring. Alfred refused at first but when told Saunders came around, Alfred capitulated.""",
        "choices": [
            {"text": "Expose the ring", "goto": "S-8"},
            {"text": "Keep quiet", "goto": "S-9"}
        ]
    },

    "S-5": {
        "character": "Saunders",
        "text": """Outraged, thought telling of dishonest offer would rouse community. Astonished - respectable element does nothing. School built across tracks. Public growls, does nothing. Alfred grouches but Saunders knows lad respects honesty. Offer from famous New York architectural firm.

Little girl killed crossing tracks to new building. Indignation elects complete reform ticket including Saunders as alderman. Alfred now off Saunders's hands. But Marge needs money for singing studies in Boston. Barton Brothers approaches Saunders with Cleveland offer - thorough training in modern merchandising.""",
        "choices": [
            {"text": "Stay at Braley's and finance Marge", "goto": "S-10"},
            {"text": "Accept Cleveland offer", "goto": "S-11"}
        ]
    },

    "S-6": {
        "character": "Saunders",
        "text": """Got car but didn't get girl - she's interested in Jed. Carol (home in New York, summers in Franklin) had been briefly engaged to Jed. When Saunders discovered enjoying Carol's company despite loving Helen, Helen eloped with Jed. In loneliness turns more to mercurial Carol. Strange glamorous creature interested in him. Still in love with Helen (can't have). Enjoys Carol, reason to believe her father would advance son-in-law's career.""",
        "choices": [
            {"text": "Ask Carol to marry him", "goto": "S-12"},
            {"text": "Don't ask Carol", "goto": "S-13"}
        ]
    },

    "S-7": {
        "character": "Saunders",
        "text": """Mr. Braley found young man after own heart, raised salary. Little play-boy in Saunders - early years turning nickel twice before spending bitterly hard. Kept away from young people. Barton Brothers opens permanent Franklin branch. Offers Saunders managership with limitless advancement. New position direct competition with Braley. Departure serious blow to old man like father to him.""",
        "choices": [
            {"text": "Accept Barton Brothers offer", "goto": "S-14"},
            {"text": "Stay with Braley", "goto": "S-15"}
        ]
    },

    "S-8": {
        "character": "Saunders",
        "text": """Goes to Donovan threatening exposure if doesn't build according to original plans. Donovan points out has something on Saunders, will use. Carries story to opposition party editor. Franklin rings with scandal. Saunders quickly involved - exposed. Outraged citizens lump Saunders with aldermen. Mrs. Mead can't hold up head, Alfred runs away. Mr. Braley only one who understood Saunders's position. When dies years later, leaves Saunders interest in store. Alfred develops talent for verse-making in wandering life.""",
        "ending": "Proving to make success in crime must put whole soul into it. People raised honest would better resign to remaining honest."
    },

    "S-9": {
        "character": "Saunders",
        "text": """After school built, Mrs. Mead, Marge, Jimmie bursting with pride. Neither Saunders nor Alfred can look without sinking heart. Donovan obtains Alfred position with New York contracting firm. Mr. Braley dies couple years later. Saunders thrown out. Alfred gets him position in business office. Whole Mead family moves to city. Surprised at change in Alfred - earns stupendous money, spends ostentatiously. Saunders's work includes shutting eyes to shady practices. Alfred marries firm member's daughter. Margery becomes social climber. Jimmie main interest of Saunders's life.""",
        "ending": "Going in for crooked practices meant whole family had plenty money. Jimmie too young to know kept integrity. Only 3/4 of brothers and sisters went bad."
    },

    "S-10": {
        "character": "Saunders",
        "text": """First time Marge's name in New York papers great occasion. 6 years before Marge can pay own way. Saunders draws long breath of relief. Didn't get expected increases. With Marge off hands, Alfred doing well and married, store safe, Saunders can think about own future. Long-cherished dream: year at Harvard studying business management.

Jimmie chooses this moment to make highest grade in Franklin high school history. Principal: 'Saunders, you must send this boy to college, not allow brilliant future sacrificed as yours was.'""",
        "choices": [
            {"text": "Give up study to send Jimmie to college", "goto": "S-16"},
            {"text": "Set Jimmie to work and go to Harvard", "goto": "S-17"}
        ]
    },

    "S-11": {
        "character": "Saunders",
        "text": """After 2 years able to send for family to Cleveland. Earning very good salary. Cleveland headquarters. Marge fits herself as singing teacher, obtains good position. Jimmie goes to Antioch College where can be self-supporting.

First tragedy indirect result of move. Alfred piles whole family into car to visit. Collision on Cleveland outskirts - Alfred killed, wife seriously injured. As soon as Alfred's wife can move from hospital, comes to Mead house. When well enough to go home, Meads all beg her remain permanently.""",
        "ending": "Saunders later married brother's widow, kept in family circle one always dearly loved. Mead family lived happy fairly prosperous life, all considering Saunders most wonderful man in world."
    },

    "S-12": {
        "character": "Saunders",
        "text": """Could hardly believe Carol marrying him until actually in Franklin Episcopal Church. Always looked on marriage as preliminary to quiet domestic life but settling down postponed: European honeymoon, finding New York apartment, winter of entertaining, terrible to-do with baby arrival, motor accident, nervous breakdown for Carol.

Poor Saunders obligated to send regular sums to mother and make good in father-in-law's brokerage office. Carol naturally expected to be center of life she created - surprised, hurt, indignant. Felt fully justified taking on constant escort: young poet. Little later wished poet back - successor titled European arrested for raising to $500 a $5 check she gave him at track.

Carol tells Saunders going to Bermuda with Elwells. Saunders doesn't trust either, thinks bad influence. Unable to leave business and go with party, foresees Carol will get in trouble again.""",
        "choices": [
            {"text": "Forbid Carol's going to Bermuda", "goto": "S-18"},
            {"text": "Don't interfere", "goto": "S-19"}
        ]
    },

    "S-13": {
        "character": "Saunders",
        "text": """Can't accept Carol as substitute for Helen. Plunges into work for forgetfulness. Very soon becomes junior partner. When Braley dies, able to buy in rest of stock. Store growing more prosperous under direction, now has income about $10,000 yearly.

5 years after Helen eloped with Jed, she again comes into Saunders's life. Jed died leaving Helen struggling to support child. Saunders loves Helen more than ever. Asks her to marry him. She tells him honestly would be glad to marry for child's sake but wants him to understand clearly what she feels is gratitude, not love.""",
        "choices": [
            {"text": "Marry Helen under these circumstances", "goto": "S-20"},
            {"text": "Don't marry Helen", "goto": "S-21"}
        ]
    },

    "S-14": {
        "character": "Saunders",
        "text": """Might not have had courage to leave Braley if foreseen effect on old man. Braley getting into difficulties. Goes into bankruptcy year later. Saunders's firm buys his store. Old man's spirit broken.

Saunders's work so fine, soon given position in main New York office. Becomes stockholder, director, finally vice-president. At 49 free at last to take up social life, decides time to marry. Florence Lamont some time associated in mind with this step. Belongs to old family, charming in kindliness and culture.

With middle-aged deliberation preparing to propose when Miss Lamont's orphan niece Mahalia Lamont shoots like comet across horizon. Wild mad love for beautiful girl. One part says 'no fool like old fool,' another says 'only one life to live.' Reasonably sure Mahalia would marry him - tired of being poor relation.""",
        "choices": [
            {"text": "Marry Florence (aunt)", "goto": "S-22"},
            {"text": "Marry Mahalia (niece)", "goto": "S-23"}
        ]
    },

    "S-15": {
        "character": "Saunders",
        "text": """Things looked black for Braley's store after new store opened. Saunders saw Braley's must adopt new merchandising policy. Made old conservative store into up-to-date paying concern. When died, left interest in store to Saunders.

Saunders begins considering marriage. Helen refuses and he definitely puts aside all hope of ever winning her. Since no longer dreamed of Helen, became more interested in other girls. Suddenly became aware of Ada Winters. Sister Marge brought Ada home to supper one night. As Saunders saw wistful little face across table, seemed like child looking through window at party she couldn't share. Had sad life. Supposed too sensitive but couldn't help things hurting her. Little girl brought out all Saunders's tenderness.""",
        "choices": [
            {"text": "Marry Ada", "goto": "S-24"},
            {"text": "Don't marry Ada", "goto": "S-25"}
        ]
    },

    "S-16": {
        "character": "Saunders",
        "text": """Jimmie did so well Saunders didn't regret sacrificing own belated chance of study. By time Jimmie graduated, decided not too late to supplement practical knowledge with business course. Before spoke to mother, excited letter from Marge - finally made enough money for winter in Paris which singer must have, wants to take mother. Plan open secret among Alfred, Marge, mother. Marge and Alfred determined mother should have good time. Could Saunders make up rest?

Saunders ashamed of taking mother for granted. Over protests sent her abroad with Marge. Upon return, arranged Mrs. Mead stay with Marge in New York. Went to New York to live with them. Eventually became head of one minor departments but didn't rise to any position of power. Saunders never married.""",
        "ending": "Consequence of years hard work for others: Alfred, Marge, Jimmie all had brilliant careers and mother had heart's desire."
    },

    "S-17": {
        "character": "Saunders",
        "text": """When Saunders left Braley's for Harvard study, everybody moved up one peg. Jimmie hated it as much as Alfred had. Saunders (with good Harvard record and years practical experience) offered position at Marshall Field's in Chicago. Sent for mother and Jimmie. Mrs. Mead had pictures and music. Jimmie studied railroad engineering, became self-supporting. When left to work on Central America railroad, Saunders first time in life without family responsibilities. Married college girl good many years younger.""",
        "ending": "Consequence of early sacrifices for family and belated recognition something due himself: others got better start but he didn't entirely lose out. Married later than most men but maybe married more wisely."
    },

    "S-18": {
        "character": "Saunders",
        "text": """Put foot down. Like good old-fashioned husband sternly forbade Carol accompanying Elwells to Bermuda. When Carol went in hysterics to father, Mr. Lane backed up husband's fiat. Having once adopted stern-husband role, Saunders found must keep it up indefinitely. Carol fell dramatically into complementary role of obedient wife. Developed marvelous ability putting husband in wrong.""",
        "ending": "Saunders never looked at any other woman. General feeling among friends Mead didn't understand wife. In later years often spoken of as 'poor Mrs. Mead.'"
    },

    "S-19": {
        "character": "Saunders",
        "text": """Before Carol left for Bermuda, Saunders had long talk. Told her didn't agree with father's attitude toward women. Carol deeply touched. Carol returned unexpectedly week before Elwells. When Elwells returned however, trouble. Mrs. Elwell insulted Carol, threatening to name Carol as co-respondent in divorce suit.

Saunders learned Mrs. Elwell had indeed started divorce suit, named Carol, had ample evidence. Faced Carol who after terrific scene, tearfully admitted guilt, putting all blame on Elwell. Begged Saunders stand by her.""",
        "choices": [
            {"text": "Insist on divorce", "goto": "S-26"},
            {"text": "Don't divorce Carol", "goto": "S-27"}
        ]
    },

    "S-20": {
        "character": "Saunders",
        "text": """When Saunders married Helen believed if good, kind, patient enough Helen would learn to love him. Though child soon adored stepfather, Helen's heart buried in Jed's grave. To amazement Helen begged off weekend in city. Utterly discouraged.

Gave party anyway. Found only Carol free that evening. Carol poured out troubles. Marriage disappointment, getting divorce. Saunders at best when people in trouble. Became so absorbed didn't go to theater but to Carol's apartment. Following day (Sunday) motoring. As always Carol's spirits rose.

Not very long before realized Carol willing to make up for wife's coldness. Wondered whether not justified seeking ephemeral love more spontaneous than wife's dutiful acquiescence.""",
        "choices": [
            {"text": "Have love-affair with Carol", "goto": "S-28"},
            {"text": "Don't have affair", "goto": "S-29"}
        ]
    },

    "S-21": {
        "character": "Saunders",
        "text": """Too intelligent to marry Helen (who didn't love him) just as too intelligent to marry Carol (whom didn't love). But since Helen still guiding star, wouldn't marry any other woman. Later came to feel no woman could be expected to adapt to old-bachelor ways. Brothers and sisters, later nieces and nephews devoted to him. Helen's boy (called him 'Uncle') very dear to him. Eventually took him into store, made junior partner.""",
        "ending": "Consequence of being so particular whom married: had joys of unclehood without disappointments and responsibilities of fatherhood. Raised unclehood to fine art."
    },

    "S-22": {
        "character": "Saunders",
        "text": """As Mahalia's uncle (for such became by marrying Aunt Florence), Saunders found girl less entrancing. Indeed grew indignant seeing how greatly irresponsibility worried aunt. Last illusion vanished when she married man of 50 for money - man hadn't any. Saunders soon retired from active business, took trip with wife to China where bought rare porcelains. Westchester house became center for collectors and explorers.""",
        "ending": "Consequence of making fortune and marrying suitable wife: few years delightful companionship, pleasant sense of security, marvelous porcelain collection willed to museum."
    },

    "S-23": {
        "character": "Saunders",
        "text": """Not until married to Mahalia realized how heavy and inelastic had become. Couldn't keep up with young wife. Mahalia said decisively two children enough, hired governess. Usually sent for Aunt Florence to keep husband company when herself going off on parties. Prudently left bulk of estate in trust for infant children but gave porcelain collection to wife as part of house furnishings.""",
        "ending": "After Saunders's death, Mahalia, though intended carrying out wishes, being pressed for money to pay for string of pearls, obliged to sell porcelains for fraction of value."
    },

    "S-24": {
        "character": "Saunders",
        "text": """First few weeks after marriage to Saunders, Ada radiant. But old habit of being hurt when things went wrong too strong to easily break. During depression fits clung pathetically. One longing: escape from Franklin. Saunders concluded duty to take her to place where could form new habits. Sold business, bought small unsuccessful mail-order business in New York.

About time prosperity began coming back to business, Ada became discouraged with slow progress at art school. Moreover lonely in evening when Saunders shut away with work. Just when Saunders able to see way clearly ahead, Ada gave up art school completely, began active campaign to return to Franklin. Desperately homesick. Played trump card: told Saunders baby coming. Wept so incessantly Saunders afraid bad for child.

Ada's parents offered position in Franklin bank. Not very good one but Saunders knew could work up quickly. But on other hand liked mail-order business, saw fortune in it he could never make in Franklin.""",
        "choices": [
            {"text": "Move back to Franklin for Ada", "goto": "S-30"},
            {"text": "Stay in New York despite Ada", "goto": "S-31"}
        ]
    },

    "S-25": {
        "character": "Saunders",
        "text": """Tried to break off tactfully when saw Ada wanted to marry him but hadn't reckoned with tenacity of nature. Bombarded with telephone calls, broken-hearted little notes. When finally consented to go to her home for one last interview, greatly embarrassed by going down on knees. When started to leave, violent hysterics, declared would kill self.

Next morning all over town poor Ada locked self in room and turned on gas. After this sent her to make long visit to relative in Western city where married Spaniard. Saunders sent beautiful wedding gift, married darned nice, sensible, plain, intelligent girl.""",
        "ending": "Children brought up in harmonious atmosphere had no nerves but much intelligence, health, joy in living. Normal American family - no conflict in this sort of family."
    },

    "S-26": {
        "character": "Saunders",
        "text": """Divorce obtained in Paris with maximum expense and minimum publicity. Carol stayed abroad with children. Saunders had to leave father-in-law's office. Naturally home-loving man, bitterly lonely. While in Franklin took occasion to call on Helen. Change in her shocked him. Instead of supporting self, become sycophant. Reflected were things to be said for Carol.

Next year went to Paris to see children and straighten out Carol's financial affairs. Spent terrible evenings over bank-book. Saw Carol not one to fend for self. When four together like old times. Saunders couldn't bear thought of lonely life and suggested remarriage. Surprised and delighted at Carol's gratitude.""",
        "ending": "Second marriage worked out more satisfactorily than first because conscious of mutual need of each other."
    },

    "S-27": {
        "character": "Saunders",
        "text": """Carol's reputation saved partly because Elwells had emotional reconciliation and went abroad but more because people said if any truth in rumors, man like Mr. Mead never would have forgiven wife. Carol (frightened and repentant) became all wife and mother. When that palled, took courses in poetry and psychology. Saunders insisted she and children spend long summers in wholesome atmosphere of Franklin which all loved.""",
        "ending": "Consequence of making best of poor bargain: worked till accumulated enough to retire on, bought beautiful tract, built house wonder of neighborhood. He and Carol went abroad on trips collecting treasures for home."
    },

    "S-28": {
        "character": "Saunders",
        "text": """Immediate effect of Saunders's love-affair with Carol unexpected relaxation of strain between him and Helen. No longer demanded warm-hearted response. Yet resentment grew that woman for whom done so much gave grudging return. When Helen did accidentally discover unfaithfulness, astonished at fury. Hope died within Saunders. Saw had taken refuge in love of dead husband to escape committing to obligations. In despair offered divorce with alimony which accepted.

This destroyed love-affair with Carol. Many years no interest in women but filled place by interesting self more than ever in younger brothers and sister. Developed mail-order business. Eventually moved enterprise to New York. About 10 years after divorce married private secretary - plain smartly dressed young woman who knew ways, willing to adapt.""",
        "ending": "Consequence of fairly consistent effort (with one backsliding) to do right by both self and group: finally made marriage based on frankness and mutual confidence, developed satisfying home life with delightful children."
    },

    "S-29": {
        "character": "Saunders",
        "text": """Refusing to solace loneliness with Carol's light love, decided romantic love not for him, turned all attention to business, almost forgetting wife's existence. Curiously had good effect - Helen type who stands up bravely against adversities but unhappy in life of ease. Been irked by Saunders's excess devotion. Felt like fly struggling in honey-pot.

Saunders thought situation at home entirely his fault until had reassuring knowledge Carol found him lovable, reinforced by satisfaction of having resisted temptation. Made him less of doormat. Helen, sensing difference, got on better. Had more respect for him when had more respect for self.""",
        "ending": "Consequence: Wicked Carol done good deed in making love to man unhappily married, thus giving back self-esteem and enabling to hold own against unappreciative wife."
    },

    "S-30": {
        "character": "Saunders",
        "text": """Not easy to become absorbed in bank work when returned to Franklin because Ada wanted to leave New York. Been uprooted from store, uprooted again from mail-order business just as becoming exciting. Gradually accepted fate, settled again into Franklin life. Conservative banking intolerably dull, relieved tedium by little real-estate speculation, at which moderately successful. Took up bridge and golf. Ada complained was golf widow in summer and bridge widow in winter.

Saunders knew had it in him to fill far bigger position than ever achieved in Franklin. Nagging sense of unused capacities made him difficult to live with.""",
        "ending": "Looked upon as successful citizen but in heart felt was failure, ashamed weakly allowed wife to wreck splendid business career. Consequence of being too good-natured to oppose rule of infantile and unreasonable person."
    },

    "S-31": {
        "character": "Saunders",
        "text": """When Ada began campaign to return there, Saunders realized takes two to make successful marriage. Saw this little fragile creature all her life used weakness and unhappiness as weapon to secure own way. But Saunders had no intention being led by nose. Sent Ada home to parents to stay until after baby born. By time baby old enough to travel, Ada longing to get away from Franklin again. Settled with little family in Montclair, New Jersey, commuting to New York.

Ada made friends among other young mothers, things went better, although marriage always far from ideal. Saunders's interest more and more in business which flourished. Ada so jealous of other women simpler for Saunders to keep out of social life.""",
        "ending": "Consequence: interest centered on son and business. Because of careful attention gave both, one companionable and other succeeded. Saunders able to give Ada long European health resort sojourns, with equanimity bear her returns home."
    }
}
