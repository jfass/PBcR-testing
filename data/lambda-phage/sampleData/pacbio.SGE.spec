# original asm settings
utgErrorRate = 0.25
utgErrorLimit = 4.5

cnsErrorRate = 0.25
cgwErrorRate = 0.25
ovlErrorRate = 0.25

merSize=14

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
