from ZeroSuppression import ConfigGen

zsgen = ConfigGen("config/2stream_5hz_100adc_allfem.fcl","config/newconfig.fcl")

zsgen.SetLoadThresholdMean(2)
zsgen.SetLoadThresholdVariance(3)
zsgen.SetPresample(7)
zsgen.SetPostsample(7)
zsgen.SetBaseThreshold(30)
zsgen.SetBasePolarity(1)

zsgen.InitThresholdMap()
zsgen.InitPolarityMap()

for crate in range(2,9):
  for card in xrange(zsgen.GetNumberOfModules(crate)):
    slot = card + zsgen.GetFirstModule(crate)
    for channel in xrange(32):
      if channel % 2 == 0:
        zsgen.SetChannelThreshold(crate,slot,channel,25)
        zsgen.SetChannelPolarity(crate,slot,channel,2)
      else:
        zsgen.SetChannelThreshold(crate,slot,channel,15)
        zsgen.SetChannelPolarity(crate,slot,channel,3)

for card in xrange(zsgen.GetNumberOfModules(1)):
  slot = card + zsgen.GetFirstModule(1)
  for channel in xrange(zsgen.GetNumberOfChannels(1,slot)):
    zsgen.SetChannelThreshold(1,slot,channel,25)
    zsgen.SetChannelPolarity(1,slot,channel,2)

for card in xrange(zsgen.GetNumberOfModules(9)):
  slot = card + zsgen.GetFirstModule(9)
  for channel in xrange(zsgen.GetNumberOfChannels(9,slot)):
    zsgen.SetChannelThreshold(9,slot,channel,15)
    zsgen.SetChannelPolarity(9,slot,channel,3)

for slot in range(16,19):
  for channel in xrange(32):
    if channel % 2 == 0:
      zsgen.SetChannelThreshold(9,slot,channel,25)
      zsgen.SetChannelPolarity(9,slot,channel,2)
    else:
      zsgen.SetChannelThreshold(9,slot,channel,15)
      zsgen.SetChannelPolarity(9,slot,channel,3)
  for channel in range(32,64):
    zsgen.SetChannelThreshold(9,slot,channel,30)
    zsgen.SetChannelPolarity(9,slot,channel,1)

zsgen.GenConfig()

