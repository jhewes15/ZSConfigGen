from ZeroSuppression import ConfigGen

zsgen = ConfigGen("./config/2stream_5hz_100adc_allfem.fcl","./config/output_config.fcl")

zsgen.SetLoadThresholdMean(10)
zsgen.SetLoadThresholdVariance(100)
zsgen.SetPresample(2)
zsgen.SetPostsample(3)
zsgen.SetBaseThreshold(50)

zsgen.InitThresholdMap()
zsgen.InitPolarityMap()

zsgen.SetChannelThreshold(2,12,40,100)
zsgen.SetPolarity(2,12,2)

zsgen.GenConfig()