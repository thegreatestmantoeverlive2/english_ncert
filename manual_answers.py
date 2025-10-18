
import json
import os

def create_memories_of_childhood():
    answers_dir = 'answers'
    if not os.path.exists(answers_dir):
        os.makedirs(answers_dir)

    answers = [
        {
            "question": "What was the first day in the land of apples like?",
            "answer": "The first day in the land of apples was a bitter-cold one.",
            "extract": "The first day in the land of apples was a bitter-cold one; for the snow still covered the ground, and the trees were bare.",
            "citation": "Memories of Childhood.md#L3:1"
        },
        {
            "question": "What still covered the ground?",
            "answer": "The snow still covered the ground.",
            "extract": "for the snow still covered the ground, and the trees were bare.",
            "citation": "Memories of Childhood.md#L3:1"
        },
        {
            "question": "What was the state of the trees?",
            "answer": "The trees were bare.",
            "extract": "and the trees were bare.",
            "citation": "Memories of Childhood.md#L3:1"
        },
        {
            "question": "What rang for breakfast?",
            "answer": "A large bell rang for breakfast.",
            "extract": "A large bell rang for breakfast, its loud metallic voice crashing through the belfry overhead and into our sensitive ears.",
            "citation": "Memories of Childhood.md#L4:1"
        },
        {
            "question": "What was its voice like?",
            "answer": "Its voice was a loud metallic voice.",
            "extract": "its loud metallic voice crashing through the belfry overhead and into our sensitive ears.",
            "citation": "Memories of Childhood.md#L4:1"
        },
        {
            "question": "What did the annoying clatter of shoes on bare floors give the narrator?",
            "answer": "The annoying clatter of shoes on bare floors gave the narrator no peace.",
            "extract": "The annoying clatter of shoes on bare floors gave us no peace.",
            "citation": "Memories of Childhood.md#L5:1"
        },
        {
            "question": "What made a bedlam within which the narrator was securely tied?",
            "answer": "The constant clash of harsh noises, with an undercurrent of many voices murmuring an unknown tongue, made a bedlam within which the narrator was securely tied.",
            "extract": "The constant clash of harsh noises, with an undercurrent of many voices murmuring an unknown tongue, made a bedlam within which I was securely tied.",
            "citation": "Memories of Childhood.md#L6:1"
        },
        {
            "question": "What did the narrator's spirit do?",
            "answer": "The narrator's spirit tore itself in struggling for its lost freedom.",
            "extract": "And though my spirit tore itself in struggling for its lost freedom, all was useless.",
            "citation": "Memories of Childhood.md#L7:1"
        },
        {
            "question": "What was the result of the spirit's struggle?",
            "answer": "The result of the spirit's struggle was useless.",
            "extract": "all was useless.",
            "citation": "Memories of Childhood.md#L7:1"
        },
        {
            "question": "Who came up after the group of girls?",
            "answer": "A paleface woman, with white hair, came up after the group of girls.",
            "extract": "A paleface woman, with white hair, came up after us.",
            "citation": "Memories of Childhood.md#L9:1"
        },
        {
            "question": "Where were the girls placed?",
            "answer": "The girls were placed in a line of girls who were marching into the dining room.",
            "extract": "We were placed in a line of girls who were marching into the dining room.",
            "citation": "Memories of Childhood.md#L10:1"
        },
        {
            "question": "What were these Indian girls wearing?",
            "answer": "These Indian girls were wearing stiff shoes and closely clinging dresses.",
            "extract": "These were Indian girls, in stiff shoes and closely clinging dresses.",
            "citation": "Memories of Childhood.md#L11:1"
        },
        {
            "question": "What did the small girls wear?",
            "answer": "The small girls wore sleeved aprons and shingled hair.",
            "extract": "The small girls wore sleeved aprons and shingled hair.",
            "citation": "Memories of Childhood.md#L12:1"
        },
        {
            "question": "How did the narrator walk?",
            "answer": "The narrator walked noiselessly in her soft moccasins.",
            "extract": "As I walked noiselessly in my soft moccasins, I felt like sinking to the floor, for my blanket had been stripped from my shoulders.",
            "citation": "Memories of Childhood.md#L13:1"
        },
        {
            "question": "What did she feel like doing?",
            "answer": "She felt like sinking to the floor.",
            "extract": "I felt like sinking to the floor, for my blanket had been stripped from my shoulders.",
            "citation": "Memories of Childhood.md#L13:1"
        },
        {
            "question": "Why did she feel like sinking to the floor?",
            "answer": "She felt like sinking to the floor because her blanket had been stripped from her shoulders.",
            "extract": "for my blanket had been stripped from my shoulders.",
            "citation": "Memories of Childhood.md#L13:1"
        },
        {
            "question": "Who did the narrator look hard at?",
            "answer": "The narrator looked hard at the Indian girls.",
            "extract": "I looked hard at the Indian girls, who seemed not to care that they were even more immodestly dressed than I, in their tightly fitting clothes.",
            "citation": "Memories of Childhood.md#L14:1"
        },
        {
            "question": "What did these girls seem not to care about?",
            "answer": "These girls seemed not to care that they were even more immodestly dressed than the narrator, in their tightly fitting clothes.",
            "extract": "who seemed not to care that they were even more immodestly dressed than I, in their tightly fitting clothes.",
            "citation": "Memories of Childhood.md#L14:1"
        },
        {
            "question": "Where did the boys enter from?",
            "answer": "The boys entered from an opposite door.",
            "extract": "While we marched in, the boys entered at an opposite door.",
            "citation": "Memories of Childhood.md#L15:1"
        },
        {
            "question": "Who did the narrator watch for?",
            "answer": "The narrator watched for the three young braves who came in her party.",
            "extract": "I watched for the three young braves who came in our party.",
            "citation": "Memories of Childhood.md#L16:1"
        },
        {
            "question": "Where did she spy them?",
            "answer": "She spied them in the rear ranks.",
            "extract": "I spied them in the rear ranks, looking as uncomfortable as I felt.",
            "citation": "Memories of Childhood.md#L17:1"
        },
        {
            "question": "How were they looking?",
            "answer": "They were looking as uncomfortable as she felt.",
            "extract": "looking as uncomfortable as I felt.",
            "citation": "Memories of Childhood.md#L17:1"
        },
        {
            "question": "What was tapped?",
            "answer": "A small bell was tapped.",
            "extract": "A small bell was tapped, and each of the pupils drew a chair from under the table.",
            "citation": "Memories of Childhood.md#L18:1"
        },
        {
            "question": "What did each of the pupils do?",
            "answer": "Each of the pupils drew a chair from under the table.",
            "extract": "and each of the pupils drew a chair from under the table.",
            "citation": "Memories of Childhood.md#L18:1"
        },
        {
            "question": "What did the narrator do, supposing this act meant they were to be seated?",
            "answer": "The narrator pulled out her chair and at once slipped into it from one side.",
            "extract": "Supposing this act meant they were to be seated, I pulled out mine and at once slipped into it from one side.",
            "citation": "Memories of Childhood.md#L19:1"
        },
        {
            "question": "What did she see when she turned her head?",
            "answer": "When she turned her head, she saw that she was the only one seated, and all the rest at her table remained standing.",
            "extract": "But when I turned my head, I saw that I was the only one seated, and all the rest at our table remained standing.",
            "citation": "Memories of Childhood.md#L20:1"
        },
        {
            "question": "What did she do as she began to rise?",
            "answer": "As she began to rise, she looked shyly around to see how chairs were to be used.",
            "extract": "Just as I began to rise, looking shyly around to see how chairs were to be used, a second bell was sounded.",
            "citation": "Memories of Childhood.md#L21:1"
        },
        {
            "question": "What was sounded then?",
            "answer": "A second bell was sounded then.",
            "extract": "a second bell was sounded.",
            "citation": "Memories of Childhood.md#L21:1"
        },
        {
            "question": "What did the narrator have to do?",
            "answer": "The narrator had to crawl back into her chair again.",
            "extract": "All were seated at last, and I had to crawl back into my chair again.",
            "citation": "Memories of Childhood.md#L22:1"
        },
        {
            "question": "What did she hear at one end of the hall?",
            "answer": "She heard a man’s voice at one end of the hall.",
            "extract": "I heard a man’s voice at one end of the hall, and I looked around to see him.",
            "citation": "Memories of Childhood.md#L23:1"
        },
        {
            "question": "What did all the others do?",
            "answer": "All the others hung their heads over their plates.",
            "extract": "But all the others hung their heads over their plates.",
            "citation": "Memories of Childhood.md#L24:1"
        },
        {
            "question": "Whose eyes did the narrator catch as she glanced at the long chain of tables?",
            "answer": "The narrator caught the eyes of a paleface woman upon her.",
            "extract": "As I glanced at the long chain of tables, I caught the eyes of a paleface woman upon me.",
            "citation": "Memories of Childhood.md#L25:1"
        },
        {
            "question": "What did she do immediately?",
            "answer": "She immediately dropped her eyes.",
            "extract": "Immediately I dropped my eyes, wondering why I was so keenly watched by the strange woman.",
            "citation": "Memories of Childhood.md#L26:1"
        },
        {
            "question": "What did the man cease?",
            "answer": "The man ceased his mutterings.",
            "extract": "The man ceased his mutterings, and then a third bell was tapped.",
            "citation": "Memories of Childhood.md#L27:1"
        },
        {
            "question": "What was tapped then?",
            "answer": "A third bell was tapped then.",
            "extract": "and then a third bell was tapped.",
            "citation": "Memories of Childhood.md#L27:1"
        },
        {
            "question": "What did every one do?",
            "answer": "Every one picked up his knife and fork and began eating.",
            "extract": "Every one picked up his knife and fork and began eating.",
            "citation": "Memories of Childhood.md#L28:1"
        },
        {
            "question": "What did the narrator do instead?",
            "answer": "The narrator began crying instead.",
            "extract": "I began crying instead, for by this time I was afraid to venture anything more.",
            "citation": "Memories of Childhood.md#L29:1"
        },
        {
            "question": "Why did she begin crying?",
            "answer": "She began crying because by this time she was afraid to venture anything more.",
            "extract": "for by this time I was afraid to venture anything more.",
            "citation": "Memories of Childhood.md#L29:1"
        },
        {
            "question": "What was not the hardest trial in that first day?",
            "answer": "The eating by formula was not the hardest trial in that first day.",
            "extract": "But this eating by formula was not the hardest trial in that first day.",
            "citation": "Memories of Childhood.md#L31:1"
        },
        {
            "question": "When did Judewin give the narrator a terrible warning?",
            "answer": "Judewin gave the narrator a terrible warning late in the morning.",
            "extract": "Late in the morning, my friend Judewin gave me a terrible warning.",
            "citation": "Memories of Childhood.md#L32:1"
        },
        {
            "question": "What did Judewin know?",
            "answer": "Judewin knew a few words of English.",
            "extract": "Judewin knew a few words of English; and she had overheard the paleface woman talk about cutting our long, heavy hair.",
            "citation": "Memories of Childhood.md#L33:1"
        },
        {
            "question": "What had she overheard?",
            "answer": "She had overheard the paleface woman talk about cutting their long, heavy hair.",
            "extract": "and she had overheard the paleface woman talk about cutting our long, heavy hair.",
            "citation": "Memories of Childhood.md#L33:1"
        },
        {
            "question": "What had their mothers taught them?",
            "answer": "Their mothers had taught them that only unskilled warriors who were captured had their hair shingled by the enemy.",
            "extract": "Our mothers had taught us that only unskilled warriors who were captured had their hair shingled by the enemy.",
            "citation": "Memories of Childhood.md#L34:1"
        },
        {
            "question": "Who wore short hair among their people?",
            "answer": "Among their people, mourners wore short hair.",
            "extract": "Among our people, short hair was worn by mourners, and shingled hair by cowards!",
            "citation": "Memories of Childhood.md#L35:1"
        },
        {
            "question": "Who wore shingled hair?",
            "answer": "Among their people, cowards wore shingled hair.",
            "extract": "and shingled hair by cowards!",
            "citation": "Memories of Childhood.md#L35:1"
        },
        {
            "question": "What did they discuss for some moments?",
            "answer": "They discussed their fate for some moments.",
            "extract": "We discussed our fate some moments, and when Judewin said, “We have to submit, because they are strong,” I rebelled.",
            "citation": "Memories of Childhood.md#L37:1"
        },
        {
            "question": "What did Judewin say?",
            "answer": "Judewin said, “We have to submit, because they are strong.”",
            "extract": "and when Judewin said, “We have to submit, because they are strong,” I rebelled.",
            "citation": "Memories of Childhood.md#L37:1"
        },
        {
            "question": "How did the narrator rebel?",
            "answer": "The narrator rebelled by saying, “No, I will not submit! I will struggle first!”",
            "extract": "“No, I will not submit! I will struggle first!” I answered.",
            "citation": "Memories of Childhood.md#L39:1"
        },
        {
            "question": "What did the narrator do when no one noticed?",
            "answer": "When no one noticed, the narrator disappeared.",
            "extract": "I watched my chance, and when no one noticed, I disappeared.",
            "citation": "Memories of Childhood.md#L41:1"
        },
        {
            "question": "What had her moccasins been exchanged for?",
            "answer": "Her moccasins had been exchanged for shoes.",
            "extract": "my moccasins had been exchanged for shoes.",
            "citation": "Memories of Childhood.md#L42:1"
        },
        {
            "question": "Where did she find a large room?",
            "answer": "She found a large room by turning aside to an open door.",
            "extract": "Turning aside to an open door, I found a large room with three white beds in it.",
            "citation": "Memories of Childhood.md#L43:1"
        },
        {
            "question": "What was in the room?",
            "answer": "Three white beds were in the room.",
            "extract": "I found a large room with three white beds in it.",
            "citation": "Memories of Childhood.md#L43:1"
        },
        {
            "question": "What were the windows covered with?",
            "answer": "The windows were covered with dark green curtains.",
            "extract": "The windows were covered with dark green curtains, which made the room very dim.",
            "citation": "Memories of Childhood.md#L44:1"
        },
        {
            "question": "What did she do on her hands and knees?",
            "answer": "On her hands and knees, she crawled under the bed.",
            "extract": "On my hands and knees I crawled under the bed, and huddled myself in the dark corner.",
            "citation": "Memories of Childhood.md#L46:1"
        },
        {
            "question": "What did she do from her hiding place?",
            "answer": "From her hiding place, she peered out, shuddering with fear whenever she heard footsteps near by.",
            "extract": "From my hiding place I peered out, shuddering with fear whenever I heard footsteps near by.",
            "citation": "Memories of Childhood.md#L48:1"
        },
        {
            "question": "What were calling her name in the hall?",
            "answer": "Loud voices were calling her name in the hall.",
            "extract": "Though in the hall loud voices were calling my name, and I knew that even Judewin was searching for me, I did not open my mouth to answer.",
            "citation": "Memories of Childhood.md#L49:1"
        },
        {
            "question": "Did she open her mouth to answer?",
            "answer": "No, she did not open her mouth to answer.",
            "extract": "I did not open my mouth to answer.",
            "citation": "Memories of Childhood.md#L49:1"
        },
        {
            "question": "What happened to the steps and voices?",
            "answer": "The steps were quickened and the voices became excited.",
            "extract": "Then the steps were quickened and the voices became excited.",
            "citation": "Memories of Childhood.md#L50:1"
        },
        {
            "question": "Who entered the room?",
            "answer": "Women and girls entered the room.",
            "extract": "Women and girls entered the room.",
            "citation": "Memories of Childhood.md#L51:1"
        },
        {
            "question": "What did the narrator do?",
            "answer": "The narrator held her breath and watched them open closet doors and peep behind large trunks.",
            "extract": "I held my breath and watched them open closet doors and peep behind large trunks.",
            "citation": "Memories of Childhood.md#L52:1"
        },
        {
            "question": "What did she watch them do?",
            "answer": "She watched them open closet doors and peep behind large trunks.",
            "extract": "I held my breath and watched them open closet doors and peep behind large trunks.",
            "citation": "Memories of Childhood.md#L52:1"
        },
        {
            "question": "What did someone do to the curtains?",
            "answer": "Someone threw up the curtains.",
            "extract": "Some one threw up the curtains, and the room was filled with sudden light.",
            "citation": "Memories of Childhood.md#L53:1"
        },
        {
            "question": "What was the room filled with?",
            "answer": "The room was filled with sudden light.",
            "extract": "and the room was filled with sudden light.",
            "citation": "Memories of Childhood.md#L53:1"
        },
        {
            "question": "What does the narrator remember being done to her?",
            "answer": "The narrator remembers being dragged out.",
            "extract": "I remember being dragged out, though I resisted by kicking and scratching wildly.",
            "citation": "Memories of Childhood.md#L55:1"
        },
        {
            "question": "How did she resist?",
            "answer": "She resisted by kicking and scratching wildly.",
            "extract": "though I resisted by kicking and scratching wildly.",
            "citation": "Memories of Childhood.md#L55:1"
        },
        {
            "question": "Where was she carried?",
            "answer": "She was carried downstairs.",
            "extract": "Inspite of myself, I was carried downstairs and tied fast in a chair.",
            "citation": "Memories of Childhood.md#L56:1"
        },
        {
            "question": "What was she tied fast in?",
            "answer": "She was tied fast in a chair.",
            "extract": "and tied fast in a chair.",
            "citation": "Memories of Childhood.md#L56:1"
        },
        {
            "question": "What did the narrator do?",
            "answer": "The narrator cried aloud, shaking her head all the while.",
            "extract": "I cried aloud, shaking my head all the while until I felt the cold blades of the scissors against my neck, and heard them gnaw off one of my thick braids.",
            "citation": "Memories of Childhood.md#L58:1"
        },
        {
            "question": "What did she feel against her neck?",
            "answer": "She felt the cold blades of the scissors against her neck.",
            "extract": "until I felt the cold blades of the scissors against my neck, and heard them gnaw off one of my thick braids.",
            "citation": "Memories of Childhood.md#L58:1"
        },
        {
            "question": "What did she hear them do?",
            "answer": "She heard them gnaw off one of her thick braids.",
            "extract": "and heard them gnaw off one of my thick braids.",
            "citation": "Memories of Childhood.md#L58:1"
        },
        {
            "question": "What did she lose then?",
            "answer": "She lost her spirit then.",
            "extract": "Then I lost my spirit.",
            "citation": "Memories of Childhood.md#L59:1"
        },
        {
            "question": "What had she suffered since the day she was taken from her mother?",
            "answer": "Since the day she was taken from her mother, she had suffered extreme indignities.",
            "extract": "Since the day I was taken from my mother I had suffered extreme indignities.",
            "citation": "Memories of Childhood.md#L59:1"
        },
        {
            "question": "What had people done to her?",
            "answer": "People had stared at her.",
            "extract": "People had stared at me.",
            "citation": "Memories of Childhood.md#L60:1"
        },
        {
            "question": "What had she been tossed about in the air like?",
            "answer": "She had been tossed about in the air like a wooden puppet.",
            "extract": "I had been tossed about in the air like a wooden puppet.",
            "citation": "Memories of Childhood.md#L61:1"
        },
        {
            "question": "What was her long hair shingled like?",
            "answer": "Her long hair was shingled like a coward’s.",
            "extract": "And now my long hair was shingled like a coward’s!",
            "citation": "Memories of Childhood.md#L62:1"
        },
        {
            "question": "What did she do in her anguish?",
            "answer": "In her anguish, she moaned for her mother.",
            "extract": "In my anguish I moaned for my mother, but no one came to comfort me.",
            "citation": "Memories of Childhood.md#L63:1"
        },
        {
            "question": "Did anyone come to comfort her?",
            "answer": "No, no one came to comfort her.",
            "extract": "but no one came to comfort me.",
            "citation": "Memories of Childhood.md#L63:1"
        },
        {
            "question": "What was she now?",
            "answer": "She was now only one of many little animals driven by a herder.",
            "extract": "for now I was only one of many little animals driven by a herder.",
            "citation": "Memories of Childhood.md#L64:1"
        },
        {
            "question": "In which class was the author studying when she first experienced untouchability?",
            "answer": "The author was studying in the third class when she first experienced untouchability.",
            "extract": "When I was studying in the third class, I hadn’t yet heard people speak openly of untouchability.",
            "citation": "Memories of Childhood.md#L68:1"
        },
        {
            "question": "What hadn't she heard people speak openly of yet?",
            "answer": "She hadn't yet heard people speak openly of untouchability.",
            "extract": "I hadn’t yet heard people speak openly of untouchability.",
            "citation": "Memories of Childhood.md#L68:1"
        },
        {
            "question": "What had she already done?",
            "answer": "She had already seen, felt, experienced and been humiliated by what it is.",
            "extract": "But I had already seen, felt, experienced and been humiliated by what it is.",
            "citation": "Memories of Childhood.md#L69:1"
        },
        {
            "question": "What was she doing one day?",
            "answer": "One day, she was walking home from school.",
            "extract": "I was walking home from school one day, an old bag hanging from my shoulder.",
            "citation": "Memories of Childhood.md#L71:1"
        },
        {
            "question": "How long would it actually take to walk the distance?",
            "answer": "It would actually take ten minutes to walk the distance.",
            "extract": "It was actually possible to walk the distance in ten minutes.",
            "citation": "Memories of Childhood.md#L72:1"
        },
        {
            "question": "How long would it usually take her?",
            "answer": "It would usually take her thirty minutes at the very least to reach home.",
            "extract": "But usually it would take me thirty minutes at the very least to reach home.",
            "citation": "Memories of Childhood.md#L73:1"
        },
        {
            "question": "What would she be doing?",
            "answer": "She would be dawdling along, watching all the fun and games that were going on, all the entertaining novelties and oddities in the streets, the shops and the bazaar.",
            "extract": "It would take me from half an hour to an hour to dawdle along, watching all the fun and games that were going on, all the entertaining novelties and oddities is the streets, the shops and the bazaar.",
            "citation": "Memories of Childhood.md#L74:1"
        },
        {
            "question": "What were some of the entertaining novelties and oddities she would watch?",
            "answer": "Some of the entertaining novelties and oddities she would watch were the performing monkey, the snake which the snakecharmer kept in its box, and the cyclist who had not got off his bike for three days.",
            "extract": "The performing monkey; the snake which the snakecharmer kept in its box and displayed from time to time; the cyclist who had not got off his bike for three days, and who kept pedalling as hard as he could from break of day;",
            "citation": "Memories of Childhood.md#L76:1"
        },
        {
            "question": "What was the performing monkey doing?",
            "answer": "The performing monkey was performing.",
            "extract": "The performing monkey;",
            "citation": "Memories of Childhood.md#L76:1"
        },
        {
            "question": "What did the snakecharmer have?",
            "answer": "The snakecharmer had a snake in a box.",
            "extract": "the snake which the snakecharmer kept in its box and displayed from time to time;",
            "citation": "Memories of Childhood.md#L76:1"
        },
        {
            "question": "What did the cyclist do?",
            "answer": "The cyclist had not got off his bike for three days and kept pedalling as hard as he could from break of day.",
            "extract": "the cyclist who had not got off his bike for three days, and who kept pedalling as hard as he could from break of day;",
            "citation": "Memories of Childhood.md#L77:1"
        },
        {
            "question": "What was pinned on the cyclist's shirt?",
            "answer": "Rupee notes were pinned on the cyclist's shirt.",
            "extract": "the rupee notes that were pinned on to his shirt to spur him on;",
            "citation": "Memories of Childhood.md#L78:1"
        },
        {
            "question": "What was at the Maariyaata temple?",
            "answer": "A huge bell was hanging at the Maariyaata temple.",
            "extract": "the Maariyaata temple, the huge bell hanging there;",
            "citation": "Memories of Childhood.md#L79:1"
        },
        {
            "question": "What was being cooked in front of the temple?",
            "answer": "Pongal offerings were being cooked in front of the temple.",
            "extract": "the pongal offerings being cooked in front of the temple;",
            "citation": "Memories of Childhood.md#L80:1"
        },
        {
            "question": "What was at the dried fish stall?",
            "answer": "A statue of Gandhi was at the dried fish stall.",
            "extract": "the dried fish stall by the statue of Gandhi;",
            "citation": "Memories of Childhood.md#L81:1"
        },
        {
            "question": "What other stalls were there?",
            "answer": "There were sweet stalls and stalls selling fried snacks.",
            "extract": "the sweet stall, the stall selling fried snacks, and all the other shops next to each other;",
            "citation": "Memories of Childhood.md#L82:1"
        },
        {
            "question": "What did the street light always demonstrate?",
            "answer": "The street light always demonstrated how it could change from blue to violet.",
            "extract": "the street light always demonstrating how it could change from blue to violet;",
            "citation": "Memories of Childhood.md#L83:1"
        },
        {
            "question": "What did the narikkuravan huntergypsy have?",
            "answer": "The narikkuravan huntergypsy had his wild lemur in cages.",
            "extract": "the narikkuravan huntergypsy with his wild lemur in cages, selling needles, clay beads and instruments for cleaning out the ears — Oh, I could go on and on.",
            "citation": "Memories of Childhood.md#L84:1"
        },
        {
            "question": "What were they selling?",
            "answer": "They were selling needles, clay beads and instruments for cleaning out the ears.",
            "extract": "selling needles, clay beads and instruments for cleaning out the ears",
            "citation": "Memories of Childhood.md#L84:1"
        },
        {
            "question": "What would people from various political parties do at times?",
            "answer": "At times, people from various political parties would arrive, put up a stage and harangue us through their mikes.",
            "extract": "At times, people from various political parties would arrive, put up a stage and harangue us through their mikes.",
            "citation": "Memories of Childhood.md#L86:1"
        },
        {
            "question": "What other performances might there be?",
            "answer": "There might be a street play, or a puppet show, or a “no magic, no miracle” stunt performance.",
            "extract": "Then there might be a street play, or a puppet show, or a “no magic, no miracle” stunt performance.",
            "citation": "Memories of Childhood.md#L87:1"
        },
        {
            "question": "What was happening at the coffee clubs in the bazaar?",
            "answer": "At the coffee clubs in the bazaar, each waiter cooled the coffee, lifting a tumbler high up and pouring its contents into a tumbler held in his other hand.",
            "extract": "Even otherwise, there were the coffee clubs in the bazaar: the way each waiter cooled the coffee, lifting a tumbler high up and pouring its contents into a tumbler held in his other hand.",
            "citation": "Memories of Childhood.md#L90:1"
        },
        {
            "question": "What were some people doing in front of the shops?",
            "answer": "Some people were sitting in front of the shops chopping up onion, their eyes turned elsewhere so that they would not smart.",
            "extract": "Or the way some people sat in front of the shops chopping up onion, their eyes turned elsewhere so that they would not smart.",
            "citation": "Memories of Childhood.md#L91:1"
        },
        {
            "question": "What was growing there?",
            "answer": "An almond tree was growing there.",
            "extract": "Or the almond tree growing there and its fruit which was occasionally blown down by the wind.",
            "citation": "Memories of Childhood.md#L92:1"
        },
        {
            "question": "What would happen to its fruit occasionally?",
            "answer": "Its fruit was occasionally blown down by the wind.",
            "extract": "and its fruit which was occasionally blown down by the wind.",
            "citation": "Memories of Childhood.md#L92:1"
        },
        {
            "question": "What would all these sights taken together do?",
            "answer": "All these sights taken together would tether her legs and stop her from going home.",
            "extract": "All these sights taken together would tether my legs and stop me from going home.",
            "citation": "Memories of Childhood.md#L93:1"
        },
        {
            "question": "What would there be according to the season?",
            "answer": "According to the season, there would be mango, cucumber, sugar-cane, sweet-potato, palm-shoots, gram, palm-syrup and palm-fruit, guavas and jack-fruit.",
            "extract": "And then, according to the season, there would be mango, cucumber, sugar-cane, sweet-potato, palm-shoots, gram, palm-syrup and palm-fruit, guavas and jack-fruit.",
            "citation": "Memories of Childhood.md#L95:1"
        },
        {
            "question": "What would she see people selling every day?",
            "answer": "Every day she would see people selling sweet and savoury fried snacks, payasam, halva, boiled tamarind seeds and iced lollies.",
            "extract": "Every day I would see people selling sweet and savoury fried snacks, payasam, halva, boiled tamarind seeds and iced lollies.",
            "citation": "Memories of Childhood.md#L96:1"
        },
        {
            "question": "What was set up at the opposite corner one day?",
            "answer": "One day, a threshing floor had been set up at the opposite corner.",
            "extract": "At the opposite corner, though, a threshing floor had been set up, and the landlord watched the proceedings, seated on a piece of sacking spread over a stone ledge.",
            "citation": "Memories of Childhood.md#L98:1"
        },
        {
            "question": "Who watched the proceedings?",
            "answer": "The landlord watched the proceedings.",
            "extract": "and the landlord watched the proceedings, seated on a piece of sacking spread over a stone ledge.",
            "citation": "Memories of Childhood.md#L98:1"
        },
        {
            "question": "What were our people hard at work doing?",
            "answer": "Our people were hard at work, driving cattle in pairs, round and round, to tread out the grain from the straw.",
            "extract": "Our people were hard at work, driving cattle in pairs, round and round, to tread out the grain from the straw.",
            "citation": "Memories of Childhood.md#L99:1"
        },
        {
            "question": "Why were the animals muzzled?",
            "answer": "The animals were muzzled so that they wouldn’t help themselves to the straw.",
            "extract": "The animals were muzzled so that they wouldn’t help themselves to the straw.",
            "citation": "Memories of Childhood.md#L100:1"
        },
        {
            "question": "Who came along from the direction of the bazaar just then?",
            "answer": "Just then, an elder of our street came along from the direction of the bazaar.",
            "extract": "Just then, an elder of our street came along from the direction of the bazaar.",
            "citation": "Memories of Childhood.md#L102:1"
        },
        {
            "question": "What made the author want to double up?",
            "answer": "The manner in which the elder was walking along made the author want to double up.",
            "extract": "The manner in which he was walking along made me want to double up.",
            "citation": "Memories of Childhood.md#L103:1"
        },
        {
            "question": "What did she guess was in the packet?",
            "answer": "She guessed there was something like vadai or green banana bhajji in the packet.",
            "extract": "I guessed there was something like vadai or green banana bhajji in the packet, because the wrapping paper was stained with oil.",
            "citation": "Memories of Childhood.md#L104:1"
        },
        {
            "question": "Why did she guess this?",
            "answer": "She guessed this because the wrapping paper was stained with oil.",
            "extract": "because the wrapping paper was stained with oil.",
            "citation": "Memories of Childhood.md#L104:1"
        },
        {
            "question": "How did the elder come along?",
            "answer": "The elder came along, holding out the packet by its string, without touching it.",
            "extract": "He came along, holding out the packet by its string, without touching it.",
            "citation": "Memories of Childhood.md#L105:1"
        },
        {
            "question": "What did the author think to herself?",
            "answer": "The author thought to herself, if he holds it like that, won’t the package come undone, and the vadais fall out?",
            "extract": "I stood there thinking to myself, if he holds it like that, won’t the package come undone, and the vadais fall out?",
            "citation": "Memories of Childhood.md#L106:1"
        },
        {
            "question": "What did the elder do?",
            "answer": "The elder went straight up to the landlord, bowed low and extended the packet towards him, cupping the hand that held the string with his other hand.",
            "extract": "The elder went straight up to the landlord, bowed low and extended the packet towards him, cupping the hand that held the string with his other hand.",
            "citation": "Memories of Childhood.md#L108:1"
        },
        {
            "question": "What did the landlord do?",
            "answer": "The landlord opened the parcel and began to eat the vadais.",
            "extract": "The landlord opened the parcel and began to eat the vadais.",
            "citation": "Memories of Childhood.md#L109:1"
        },
        {
            "question": "What did the author do after she had watched all this?",
            "answer": "After she had watched all this, at last she went home.",
            "extract": "After I had watched all this, at last I went home.",
            "citation": "Memories of Childhood.md#L111:1"
        },
        {
            "question": "Who was at home?",
            "answer": "Her elder brother was at home.",
            "extract": "My elder brother was there.",
            "citation": "Memories of Childhood.md#L111:1"
        },
        {
            "question": "What did she tell him?",
            "answer": "She told him the story in all its comic detail.",
            "extract": "I told him the story in all its comic detail.",
            "citation": "Memories of Childhood.md#L112:1"
        },
        {
            "question": "What was Annan's reaction?",
            "answer": "Annan was not amused.",
            "extract": "But Annan was not amused.",
            "citation": "Memories of Childhood.md#L113:1"
        },
        {
            "question": "What did Annan tell her?",
            "answer": "Annan told her the man wasn’t being funny when he carried the package like that.",
            "extract": "Annan told me the man wasn’t being funny when he carried the package like that.",
            "citation": "Memories of Childhood.md#L114:1"
        },
        {
            "question": "Why did he have to carry the package by its string?",
            "answer": "He had to carry the package by its string because everybody believed that they were upper caste and therefore must not touch us. If they did, they would be polluted.",
            "extract": "He said everybody believed that they were upper caste and therefore must not touch us. If they did, they would be polluted. That’s why he had to carry the package by its string.",
            "citation": "Memories of Childhood.md#L115:1"
        },
        {
            "question": "How did the author feel when she heard this?",
            "answer": "When she heard this, she didn’t want to laugh any more, and she felt terribly sad.",
            "extract": "When I heard this, I didn’t want to laugh any more, and I felt terribly sad.",
            "citation": "Memories of Childhood.md#L117:1"
        },
        {
            "question": "What did she feel so provoked and angry about?",
            "answer": "She felt so provoked and angry that she wanted to touch those wretched vadais herself straightaway.",
            "extract": "I felt so provoked and angry that I wanted to touch those wretched vadais myself straightaway.",
            "citation": "Memories of Childhood.md#L118:1"
        },
        {
            "question": "What did the thought of it do to her?",
            "answer": "The thought of it infuriated her.",
            "extract": "The thought of it infuriated me.",
            "citation": "Memories of Childhood.md#L119:1"
        },
        {
            "question": "What did she wonder about these fellows?",
            "answer": "She wondered how it was that these fellows thought so much of themselves.",
            "extract": "How was it that these fellows thought so much of themselves?",
            "citation": "Memories of Childhood.md#L121:1"
        },
        {
            "question": "What did she say about her people?",
            "answer": "She said that her people should never run these petty errands for these fellows.",
            "extract": "Our people should never run these petty errands for these fellows.",
            "citation": "Memories of Childhood.md#L122:1"
        },
        {
            "question": "Who was her elder brother?",
            "answer": "Her elder brother was studying at a university.",
            "extract": "My elder brother, who was studying at a university, had come home for the holidays.",
            "citation": "Memories of Childhood.md#L124:1"
        },
        {
            "question": "Where would he often go?",
            "answer": "He would often go to the library in their neighbouring village in order to borrow books.",
            "extract": "He would often go to the library in our neighbouring village in order to borrow books.",
            "citation": "Memories of Childhood.md#L125:1"
        },
        {
            "question": "What happened one day when he was on his way home?",
            "answer": "One day when he was on his way home, walking along the banks of the irrigation tank, one of the landlord’s men came up behind him.",
            "extract": "He was on his way home one day, walking along the banks of the irrigation tank. One of the landlord’s men came up behind him.",
            "citation": "Memories of Childhood.md#L126:1"
        },
        {
            "question": "What did the landlord's man ask him?",
            "answer": "The landlord's man asked him, “Who are you, appa, what’s your name?”",
            "extract": "He thought my Annan looked unfamiliar, and so he asked, “Who are you, appa, what’s your name?”",
            "citation": "Memories of Childhood.md#L127:1"
        },
        {
            "question": "What did Annan tell him?",
            "answer": "Annan told him his name.",
            "extract": "Annan told him his name.",
            "citation": "Memories of Childhood.md#L128:1"
        },
        {
            "question": "What did the other man ask immediately?",
            "answer": "Immediately the other man asked, “Thambi, on which street do you live?”",
            "extract": "Immediately the other man asked, “Thambi, on which street do you live?”",
            "citation": "Memories of Childhood.md#L129:1"
        },
        {
            "question": "What was the point of this question?",
            "answer": "The point of this was that if he knew on which street they lived, he would know their caste too.",
            "extract": "The point of this was that if he knew on which street we lived, he would know our caste too.",
            "citation": "Memories of Childhood.md#L130:1"
        },
        {
            "question": "What did Annan add?",
            "answer": "Annan added that because they are born into this community, they are never given any honour or dignity or respect; they are stripped of all that.",
            "extract": "Annan told me all these things. And he added, “Because we are born into this community, we are never given any honour or dignity or respect; we are stripped of all that.",
            "citation": "Memories of Childhood.md#L132:1"
        },
        {
            "question": "What did he say they are stripped of?",
            "answer": "He said they are stripped of all honour, dignity, and respect.",
            "extract": "we are stripped of all that.",
            "citation": "Memories of Childhood.md#L133:1"
        },
        {
            "question": "What did he say they can do if they study and make progress?",
            "answer": "He said that if they study and make progress, they can throw away these indignities.",
            "extract": "But if we study and make progress, we can throw away these indignities.",
            "citation": "Memories of Childhood.md#L133:1"
        },
        {
            "question": "What did he tell her to do?",
            "answer": "He told her to study with care, learn all she can, and be always ahead in her lessons.",
            "extract": "So study with care, learn all you can. If you are always ahead in your lessons, people will come to you of their own accord and attach themselves to you. Work hard and learn.”",
            "citation": "Memories of Childhood.md#L134:1"
        },
        {
            "question": "What did the words that Annan spoke to her that day do?",
            "answer": "The words that Annan spoke to her that day made a very deep impression on her.",
            "extract": "The words that Annan spoke to me that day made a very deep impression on me.",
            "citation": "Memories of Childhood.md#L135:1"
        },
        {
            "question": "What did she do?",
            "answer": "She studied hard, with all her breath and being, in a frenzy almost.",
            "extract": "And I studied hard, with all my breath and being, in a frenzy almost.",
            "citation": "Memories of Childhood.md#L136:1"
        },
        {
            "question": "What was the result of her standing first in her class?",
            "answer": "The result of her standing first in her class was that many people became her friends.",
            "extract": "As Annan had urged, I stood first in my class. And because of that, many people became my friends.",
            "citation": "Memories of Childhood.md#L137:1"
        }
    ]

    filepath = os.path.join(answers_dir, 'Memories of Childhood.json')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(answers, f, indent=4)

if __name__ == '__main__':
    create_memories_of_childhood()
