overlapper = ovl
unitigger = bogart
utgBubblePopping = 1

kickOutNonOvlContigs = 1
cgwDemoteRBP = 0
cgwMergeMissingThreshold = 0.5

merSize = 14

merylMemory = 128000
merylThreads = 16

ovlStoreMemory = 8192

# grid info
useGrid = 1
scriptOnGrid = 1
frgCorrOnGrid = 1
ovlCorrOnGrid = 1

sge = -A assembly
sgeScript = -pe threads 16 
sgeConsensus = -pe threads 1 
sgeOverlap = -pe threads 2
sgeFragmentCorrection = -pe threads 2 
sgeOverlapCorrection = -pe threads 1

ovlHashBits = 24
ovlThreads = 2
ovlHashBlockLength = 20000000
ovlRefBlockSize =  50000000

frgCorrThreads = 2 
frgCorrBatchSize = 100000 

ovlCorrBatchSize = 100000

merOverlapperThreads = 6

doToggle=0
toggleNumInstances = 0
toggleUnitigLength = 2000

doOverlapBasedTrimming = 1
doExtendClearRanges = 2 
