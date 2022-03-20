import random
import numpy as np
import time

# A global constant defining the alphabet.
LCLETTERS = " abcdefghijklmnopqrstuvwxyz"
# UCLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# test1
dict1_1 = "underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con"
dict1_2 = "rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ"
dict1_3 = "yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur"
dict1_4 = "cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible"
dict1_5 = "ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s"

plain = [dict1_1, dict1_2, dict1_3, dict1_4, dict1_5]

#test2

plain_2=["lacrosses","protectional","blistered", "leaseback", "assurers", "frizzlers","submerse","rankness","moonset","farcer","brickyard","stolonic","trimmings","glottic",
         "rotates", "twirlier", "stuffer","publishable","invalided", "harshens", "tortoni", "unlikely", "alefs", "gladding","favouring", "particulate", "baldpates", "changeover",
         "lingua","proctological","freaking", "outflanked", "amulets", "imagist", "hyped","pilfers", "overachiever", "clarence", "outdates", "smeltery"]




def coin_generation_algorithm(c, L):
    return random.uniform(0, 1)


def Enc(m, K):
    L = len(m)
    ciphertext_pointer = 0
    message_pointer = 0
    num_rand_characters = 0
    prob_of_random_ciphertext = 0.75
    c = ''

    while ciphertext_pointer < L + num_rand_characters:
        coin_value = coin_generation_algorithm(ciphertext_pointer, L)

        if prob_of_random_ciphertext < coin_value <= 1:
            j = m[message_pointer]
            # c[ciphertext_pointer] = K[ord(j) - 97]
            if j != ' ':
                c = c + K[ord(j) - 96]
            else:
                c = c + K[ord(j) - 32]
            message_pointer = message_pointer + 1

        if 0 <= coin_value <= prob_of_random_ciphertext:
            ran = random.choice(' abcdefghijklmnopqrstuvwxyz')
            c = c + ran
            num_rand_characters = num_rand_characters + 1

        ciphertext_pointer = ciphertext_pointer + 1

    return c


def isLegalKey(key):
    return (len(key) == 26 and all([ch in key for ch in LCLETTERS]))


def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list(LCLETTERS)  # Turn string into list of letters
    random.shuffle(lst)  # Shuffle the list randomly
    return ''.join(lst)  # Assemble them back into a string


class decryption:
    key = None

    def __init__(self, key=makeRandomKey()):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__currentKey = key

    # def getKey(self):
    #     return self.__currentKey
    #
    # def setKey(self, newKey):
    #     """Setter for the stored key.  Check that it's a legal
    #     key."""
    #     if isLegalKey(newKey) == True:
    #         self.__currentKey = newKey

    def statistical_frequency(self, s):
        freq = [0 for i in range(27)]
        # print(s)
        for i in s:
            if i != ' ':
                freq[ord(i) - 97 + 1] += 1
            else:
                freq[0] += 1
                # print(freq)
        return freq

    # find the distance between plaintext and ciphertext
    def distance(self, p, c):
        A = self.statistical_frequency(p)
        B = self.statistical_frequency(c)

        # sort the frequency to eliminate the shifting impact
        A.sort()
        B.sort()
        C = []
        Dist = 0
        for i in range(len(A)):
            C.append((A[i] - B[i]))
            Dist = Dist + (A[i] - B[i]) ** 2

        return Dist

    def guess(self, P, C):
        gussed_plaintext_index = [0 for i in range(0, len(P))]

        for i in range(0, len(P)):
            gussed_plaintext_index[i] = (self.distance(P[i], C))
        #print(gussed_plaintext_index)

        return gussed_plaintext_index.index(min(gussed_plaintext_index))



#Encrypt the message
key=makeRandomKey()
#print(key)
cipher = Enc(plain[0], key)
print(cipher)


#decrypt the message
a = decryption()
#print(plain[0])
cipheretext = input("Enter the ciphertext: ")
test = input("is this test 1 or test 2? ")

if test== '1':
    start = time.time()
#################test1########################
    plain_index_1 = a.guess(plain, cipheretext)
    print("My plaintext guess is: ")
    print(plain[plain_index_1])
    print("The guessing time is: ")
    print(time.time()-start)

else:
    start = time.time()
###############test2########################
    plain_index_2 = a.guess(plain_2 , cipheretext)
    #print(plain_index_2)
    print("My plaintext guess is: ")
    print(plain_2[plain_index_2])
    print("The guessing time is: ")
    print(time.time() - start)





