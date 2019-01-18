import re

#text = "lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool mzer rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh"
#text = 'btnpufhz esxfh vyhvefz ufhez xsgfnafcfz umabtfz qz kmhmgsjfg ghndf tiufhzumbfz ahneez ydsdafhfzasdw uhnanbne pmdwefz lmeeumufhz oymgz tnuz kmdz vncfz pmdwfgz dmsxf ltmbq wmz zdmsez zmiz pszkfmayhf aydf zyd zumdwef vvzfz wnvvefz khfflmhf tmpzafhz bndz sdksdsasfz mpnfvmz athmztfz tmppfh tfcfz bivfhuydq gnldfg ghsxfh pmdwefh zuskki zlmv zunnksdw gfmgfh ahsxsme dyqfg kemw pmhwsdme byvsdwfg enzfhz uzfygn bhsuueflmhf bmebyemanhz gnldsdw pydwz uyzt xmc uydafg zbhffd gsf enzfh difalnhq kenlbtmhaz venbqfg ayvf vmhkz zbmw jfhnfz ggfg kemxnh vhnqf vmhkfg kemxnhz pyaafhfg tmppfhsdw byvfz befmdfg hnvyzafh kenngsdw vhfmqz zunsefhz knzzsez bhmindz yhe ufzzspmefg bhfasdz hmdgnpdfzz bhfmasndszpz zsenz jnhbtsdw bnnqsf bendf oyfzfz meaz zpnqf zuffgnpfafh ztmhflmhf'
text = 'mrsjcm jm zsgfcpcd mrtgfkcm eqgcd arm mragfcm utem mkar chcujsgf vqtpecp dcucd eai ychcm mraak sgepam mxajcd paae yarrsgf xtgfkcp eaaksgf xtupakafscm ramem zkteecp xqeecpm btkdam uaxrpcmmcm lszzscm cuya dpsncp ksgem uagmcd am mbsooksgf mkqprsgf zktf osrrcd rmcqdam rpscmeyaad wctx myckk ksgqhcm upcesgm meqdkscp uytggckm eaqpsme pawqmecp rqzzcd uyqffsgf mrsjcd mrszzscme dpqx btkj zammskm ksncme ddcd oaxwscm eaffkc wtpg dpqxm msksuag bapxyakc jkqdfsgf mupaf gcbm xqgf epakkcd mraaksgf wkaujcd kamcpm zkteecme ptncd uiukc rsrcm ksnc fpqgfcm dtcxagm nth mrtxm uyqf zakkabqrm eycapscm ytspscme mqrrape fktmmcm psr tmussm dctdcme ztptdsoc rytfc wsem mgtpjm upsrrkcbtpc mrkte xaujsgfwspd ptgdaxm mktwm wpctjsgf zaakm uptiagm'
#text = 'xugsx qgxxgkv mzxzdugezvx svuaziqx jvvsx jgit sixhvt qgyed sqzuk dbbrzuv cvx bedlvu uvfxvx ygryirgade ydfjdw lvedx svvpx adiezxa jezaarv jglggex bzukvezuk egsvt kdshvex brgaavuzuk rdxzuk yhgzuzuk hgqqvevt qgeazgux srgwsvu ovrrdx tddexadsx tdfurdgtzuk gssx tdy qgzrjdqjvt px egmvx ugaiev kedp tdfu bddasezua afvgpx vcyr jdixaedshvtdu jill ahevgt keivx qgex kezutzuk yevvszuk sixh sibbvt sdpv sedkegq jzauvax tzupve adgt brgk yrdypx uvfjzvx vrvshguazuv vrmzxh yegxhvx svxxzqgrx tzuk jezaarve yegxhvt qvag uwvafdep vt bdepvt adkkrvt jvvs xvrmgkvx vezxvx xsrgax fgrtdx adkkrvx adgttvt rgiutedqga tvqdvt sdssvt bzcvx jglgge kugerzve fhgypvt jdekx xfzllrzuk xgra jdqjzuk xyevvux sedbzrv gyyiqirgadex ydqsdx ygux jgebx tdfux sibbzuk jgutfztahx pritkv'

regexes = [re.compile(r'(\w)\1'), re.compile(r'(\w).+\1{2}'), re.compile(r'(\w)\1.+\1'), re.compile(r'^\w{3}(\w)\1'),  # doubles
               re.compile(r'(\w).+\1'), re.compile(r'(\w).+\1.+\1'), re.compile(r'(\w).\1'),  # character repeated in word
               re.compile(r'(\w)\1.+(\w)\2')]

def get_all_letters_to_decrypt(s):
    letters = set()
    for letter in s:
        letters.add(letter)
    return letters


def build_language_dictionary(fn):
    with open(fn, 'r') as fh:
        dw = [w.strip().lower() for w in fh.readlines()]
    ds = set(dw)
    return dw, ds


def get_next_words_to_target(words, min_word_length=11):
    # Build the distribution
    targets = [w for w in words if len(w) >= min_word_length]
    targets.sort(key=len, reverse=True)
    return targets


def words_with_same_length_as_given_word(words, longest):
    same_length_as_longest = []
    for word in words:
        if len(word) == len(longest):
            same_length_as_longest.append(word)
    return same_length_as_longest


def find_matching_candidate(cipherword, clearwords):
    mapping = {}
    cands = set(clearwords)
    for clear in clearwords:
        for regex in regexes:
            if not bool(regex.search(cipherword)) == bool(regex.search(clear)):
                cands.discard(clear)
                break
    if len(cands) > 1:
        return None
    else:
        return cands.pop()


def reduce_candidates_through_partial_decryption(word, possibles, m):
    partial_decryptions = []
    #print("possibles: %r" % possibles)
    for possible in possibles:
        pd = ''
        for letter in possible:
            if letter in m:
                pd = ''.join((pd, letter))
            else:
                pd = ''.join((pd, '*'))
        partial_decryptions.append((pd, edit_distance(word, pd)))
    partial_decryptions.sort(key=lambda x: x[1])
    return set(partial_decryptions[0][0]) # strongest candidate; set so that calling func can pop()


def build_mapping(word1, word2, master_mapping):
    for key_letter, target_letter in zip(word1, word2):
        if key_letter in master_mapping:
            assert master_mapping[key_letter] == target_letter
        else:
            master_mapping[key_letter] = target_letter

    return master_mapping


def decrypt(ciphertext, mapping):
    cleartext = ''
    for letter in ciphertext:
        if letter in mapping:
            cleartext = ''.join((cleartext, mapping[letter]))
        else:
            cleartext = ''.join((cleartext, '_'))
    return cleartext


def edit_distance(word1, word2):
    if len(word1) != len(word2):
        return 99
    '''
    #TODO Speed this up, it accounts for 33% of program time
    dist = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            dist += 1
    return dist
    '''
    return sum([1 for l1, l2 in zip(word1, word2) if l1 != l2 ])


def find_cleartext_word(tw, all_words):
    possible_words = []
    us_counts = 0
    for letter in tw:
        if letter == '_':
            us_counts += 1
    for word in all_words:
        if edit_distance(tw, word) == us_counts:
            possible_words.append(word)
    return possible_words


def get_count_of_unknown_letters(w):
    return sum([1 for letter in w if letter == '_'])


def run(input_string):
    mapping = {}
    ciphertext_str = input_string
    ciphertext_words_set = set(ciphertext_str.split())
    letters_to_decrypt = get_all_letters_to_decrypt(''.join(ciphertext_str.split())) # Get rid of spaces
    count_of_words_to_decrypt = len(ciphertext_words_set)

    print("# words to decrypt: %i" % count_of_words_to_decrypt)

    dictionary_words_list, dictionary_words_set = build_language_dictionary('dictionary.lst')

    next_words_to_target = get_next_words_to_target(ciphertext_words_set) # May be more than one word

    for word in next_words_to_target:
        print("Next ciphertext word to decrypt: %s" % word)
        same_length_as_longest = words_with_same_length_as_given_word(dictionary_words_set, word) # may be longer than 1
        print("\tPotential decrypted matches: %r" % same_length_as_longest)

        candidate = find_matching_candidate(word, same_length_as_longest)
        print("Candidates: %r" % candidate)

        if candidate:
            mapping = build_mapping(word, candidate, mapping)
            print("Mapping: %r" % mapping)

        for letter in mapping.keys():
            letters_to_decrypt.discard(letter)
        print("Letters remaining to decrypt: %r" % letters_to_decrypt)

    decrypted_words = set()
    for word in ciphertext_words_set:
        if '_' not in decrypt(word, mapping):
            decrypted_words.add(word)
    ciphertext_words_set = ciphertext_words_set - decrypted_words
    print("# words to decrypt: %i" % len(ciphertext_words_set))

    print(' '.join([decrypt(word, mapping) for word in ciphertext_words_set]))

    ###################
    ### SECOND HALF ###
    ###################
    while len(ciphertext_words_set) > 0:
        for word, cipher in [(decrypt(word, mapping), word) for word in ciphertext_words_set]:
            if get_count_of_unknown_letters(word) == 1:
                #TODO These two list comprehensions are the biggest time sucks of the program
                same_length = [w for w in dictionary_words_list if len(w) == len(word)]
                c = [w for w in same_length if edit_distance(word, w) == 1]
                print("%s:%r" % (word, c))
                if len(c) == 1:
                    i = word.index('_')
                    key = cipher[i]
                    v = c[0][i]
                    mapping[key] = v
                    break
                    print("%s -> %s" % (key, v))

        print(' '.join([decrypt(word, mapping) for word in ciphertext_words_set]))

        for word in ciphertext_words_set:
            if '_' not in decrypt(word, mapping):
                decrypted_words.add(word)
        ciphertext_words_set = ciphertext_words_set - decrypted_words
        print("# words to decrypt: %i" % len(ciphertext_words_set))

    mapping[' '] = ' '

    return(decrypt(ciphertext_str, mapping))

print(run(text))