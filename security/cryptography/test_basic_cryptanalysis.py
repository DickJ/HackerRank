import random
import unittest
from .basic_cryptanalysis import build_language_dictionary, decrypt, edit_distance, find_cleartext_word, \
                                 get_all_letters_to_decrypt, get_count_of_unknown_letters, run

class Tests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.dictionary_words, self.dictionary_set = build_language_dictionary('dictionary.lst')

    def tearDown(self):
        pass

    #def interTestSetUp(self):
    #    self.cleartext = ' '.join(random.sample(self.dictionary_words, 100))
    #    letters_key = list(set([letter for letter in ''.join(self.cleartext.lower().split())]))
    #    self.mapping = {' ': ' '}
    #    for i, j in zip(letters_key, random.sample(letters_key, len(letters_key))):
    #        self.mapping[i] = j
    #    self.ciphertext = decrypt(self.cleartext, self.mapping)


    def test_get_all_letters_to_decrypt(self):
        self.assertEqual(get_all_letters_to_decrypt('abcd'), {'a', 'b', 'c', 'd'})
        self.assertEqual(get_all_letters_to_decrypt('abcdcd'), {'a', 'b', 'c', 'd'})
        self.assertEqual(get_all_letters_to_decrypt('aaabbb'), {'a', 'b'})

    def test_edit_distance(self):
        self.assertEqual(edit_distance('abcd', 'abce'), 1)
        self.assertEqual(edit_distance('abcdefg', 'gfedcba'), 6)
        self.assertEqual(edit_distance('aaa', 'bbb'), 3)
        self.assertEqual(edit_distance('aaa', 'aaa'), 0)
        self.assertEqual(edit_distance('aa', 'bbb'), 99)
        self.assertEqual(edit_distance('aaa', 'bb'), 99)


    def test_decrypt(self):
        self.assertEqual(decrypt('abc', {'a': 'a', 'b':'b', 'c':'c'}), 'abc')
        self.assertEqual(decrypt('abc', {'a': 'c', 'b': 'a', 'c': 'b'}), 'cab')
        self.assertEqual(decrypt('abc', {'a': 'c', 'b': 'a'}), 'ca_')
        self.assertEqual(decrypt('abc', {}), '___')

    def test_find_cleartext_word(self):
        self.assertEqual(find_cleartext_word('p_nged', self.dictionary_set), ['pinged'])
        self.assertEqual(find_cleartext_word('p_s_rs', self.dictionary_set), ['posers'])
        self.assertEqual(find_cleartext_word('________________', self.dictionary_set), ['nanotechnologies'])
        self.assertEqual(sorted(find_cleartext_word('n_de', self.dictionary_set)), ['node', 'nude'])

    def test_get_count_of_unknown_letters(self):
        self.assertEqual(get_count_of_unknown_letters('abc'), 0)
        self.assertEqual(get_count_of_unknown_letters('a_c'), 1)
        self.assertEqual(get_count_of_unknown_letters('___'), 3)

    def test_run1(self):
        self.ciphertext = 'lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool mzer rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh'
        self.cleartext =  'skulker choke minifloppies scratched recursions hairiest boas dps twiddles orthogonal posers stoppage echo cranking roached trawling saying confusers sysop bytes punting minifloppieses patch ruder pop urchin zaps lase post bit incantation barns munches trawl newsgroups wins scrogs gnarliest arena losses compressing funkiest musics fences wanked drivers weasel dinker phases nuke driver globed biffed slops patches deltas bombed bouncing cripplewares dec tubes grunge pasties trashing hats whacking hairballs pmed drone fools urls pushing twiddle phage screen segmented foregrounded spoiler profiles blts bounced tourists clean clobbers pods gobble con cubings snailing download rfcs hose widget compacter adas glitched crumb mailbombs snark'
        self.assertEqual(run(self.ciphertext), self.cleartext)

    def test_run2(self):
        self.ciphertext = 'btnpufhz esxfh vyhvefz ufhez xsgfnafcfz umabtfz qz kmhmgsjfg ghndf tiufhzumbfz ahneez ydsdafhfzasdw uhnanbne pmdwefz lmeeumufhz oymgz tnuz kmdz vncfz pmdwfgz dmsxf ltmbq wmz zdmsez zmiz pszkfmayhf aydf zyd zumdwef vvzfz wnvvefz khfflmhf tmpzafhz bndz sdksdsasfz mpnfvmz athmztfz tmppfh tfcfz bivfhuydq gnldfg ghsxfh pmdwefh zuskki zlmv zunnksdw gfmgfh ahsxsme dyqfg kemw pmhwsdme byvsdwfg enzfhz uzfygn bhsuueflmhf bmebyemanhz gnldsdw pydwz uyzt xmc uydafg zbhffd gsf enzfh difalnhq kenlbtmhaz venbqfg ayvf vmhkz zbmw jfhnfz ggfg kemxnh vhnqf vmhkfg kemxnhz pyaafhfg tmppfhsdw byvfz befmdfg hnvyzafh kenngsdw vhfmqz zunsefhz knzzsez bhmindz yhe ufzzspmefg bhfasdz hmdgnpdfzz bhfmasndszpz zsenz jnhbtsdw bnnqsf bendf oyfzfz meaz zpnqf zuffgnpfafh ztmhflmhf'
        self.cleartext =  'chompers liver burbles perls videotexes patches ks faradized drone hyperspaces trolls uninteresting protocol mangles wallpapers quads hops fans boxes mangeds naive whack gas snails says misfeature tune sun spangle bbses gobbles freeware hamsters cons infinities amoebas thrashes hammer hexes cyberpunk downed driver mangler spiffy swab spoofing deader trivial nuked flag marginal cubinged losers pseudo crippleware calculators downing mungs push vax punted screen die loser nyetwork flowcharts blocked tube barfs scag zeroes dded flavor broke barfed flavors muttered hammering cubes cleaned robuster flooding breaks spoilers fossils crayons url pessimaled cretins randomness creationisms silos zorching cookie clone queses alts smoke speedometer shareware'
        self.assertEqual(run(self.ciphertext), self.cleartext)

    def test_run3(self):
        self.ciphertext = 'mrsjcm jm zsgfcpcd mrtgfkcm eqgcd arm mragfcm utem mkar chcujsgf vqtpecp dcucd eai ychcm mraak sgepam mxajcd paae yarrsgf xtgfkcp eaaksgf xtupakafscm ramem zkteecp xqeecpm btkdam uaxrpcmmcm lszzscm cuya dpsncp ksgem uagmcd am mbsooksgf mkqprsgf zktf osrrcd rmcqdam rpscmeyaad wctx myckk ksgqhcm upcesgm meqdkscp uytggckm eaqpsme pawqmecp rqzzcd uyqffsgf mrsjcd mrszzscme dpqx btkj zammskm ksncme ddcd oaxwscm eaffkc wtpg dpqxm msksuag bapxyakc jkqdfsgf mupaf gcbm xqgf epakkcd mraaksgf wkaujcd kamcpm zkteecme ptncd uiukc rsrcm ksnc fpqgfcm dtcxagm nth mrtxm uyqf zakkabqrm eycapscm ytspscme mqrrape fktmmcm psr tmussm dctdcme ztptdsoc rytfc wsem mgtpjm upsrrkcbtpc mrkte xaujsgfwspd ptgdaxm mktwm wpctjsgf zaakm uptiagm'
        self.cleartext =  'spikes ks fingered spangles tuned ops sponges cats slop execking quarter deced toy hexes spool intros smoked root hopping mangler tooling macrologies posts flatter mutters waldos compresses jiffies echo driver lints consed os swizzling slurping flag zipped pseudos priesthood beam shell linuxes cretins studlier channels tourist robuster puffed chugging spiked spiffiest drum walk fossils livest dded zombies toggle barn drums silicon wormhole kludging scrog news mung trolled spooling blocked losers flattest raved cycle pipes live grunges daemons vax spams chug followups theories hairiest support glasses rip asciis deadest faradize phage bits snarks crippleware splat mockingbird randoms slabs breaking fools crayons'
        self.assertEqual(run(self.ciphertext), self.cleartext)

    def test_run4(self):
        self.ciphertext = 'xugsx qgxxgkv mzxzdugezvx svuaziqx jvvsx jgit sixhvt qgyed sqzuk dbbrzuv cvx bedlvu uvfxvx ygryirgade ydfjdw lvedx svvpx adiezxa jezaarv jglggex bzukvezuk egsvt kdshvex brgaavuzuk rdxzuk yhgzuzuk hgqqvevt qgeazgux srgwsvu ovrrdx tddexadsx tdfurdgtzuk gssx tdy qgzrjdqjvt px egmvx ugaiev kedp tdfu bddasezua afvgpx vcyr jdixaedshvtdu jill ahevgt keivx qgex kezutzuk yevvszuk sixh sibbvt sdpv sedkegq jzauvax tzupve adgt brgk yrdypx uvfjzvx vrvshguazuv vrmzxh yegxhvx svxxzqgrx tzuk jezaarve yegxhvt qvag uwvafdep vt bdepvt adkkrvt jvvs xvrmgkvx vezxvx xsrgax fgrtdx adkkrvx adgttvt rgiutedqga tvqdvt sdssvt bzcvx jglgge kugerzve fhgypvt jdekx xfzllrzuk xgra jdqjzuk xyevvux sedbzrv gyyiqirgadex ydqsdx ygux jgebx tdfux sibbzuk jgutfztahx pritkv'
        self.cleartext =  'snaps massage visionaries pentiums beeps baud pushed macro pming offline xes frozen newses calculator cowboy zeros peeks tourist brittle bazaars fingering raped gophers flattening losing chaining hammered martians playpen jellos doorstops downloading apps doc mailbombed ks raves nature grok down footprint tweaks excl boustrophedon buzz thread grues mars grinding creeping push puffed poke program bitnets dinker toad flag clocks newbies elephantine elvish crashes pessimals ding brittler crashed meta nyetwork ed forked toggled beep selvages erises splats waldos toggles toadded laundromat demoed popped fixes bazaar gnarlier whacked borgs swizzling salt bombing screens profile accumulators compos cans barfs downs puffing bandwidths kludge'
        self.assertEqual(run(self.ciphertext), self.cleartext)