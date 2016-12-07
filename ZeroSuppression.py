
class ConfigGen:

  _threshold_map = []
  _polarity_map = []
  _load_threshold_mean = 10
  _load_threshold_variance = 100
  _presample = 2
  _postsample = 3
  _threshold = 50

  def __init__(self,input_config_name,output_config_name):
    self.f_in = open(input_config_name,'r')
    self.f_out = open(output_config_name,'w')

  def GenConfig(self):
    for crate in range (1,10):
      config_name = "sebAppseb0{}".format(crate)
      self.CopyUntilString(config_name)
      self.CopyUntilString("xmit:{")
      self.CopyUntilString("}")
      self.WriteHeader()
      for fem in xrange(self.GetNumberOfModules(crate)):
        self.WriteFEM(crate,fem)
      self.SyncInputFile()
    self.CopyUntilEnd()

  def WriteHeader(self):
    self.f_out.write("  zero_suppression:{{\n")
    self.f_out.write("    params:{\n")
    self.f_out.write("      load_threshold_mean : {}\n".format(self._load_threshold_mean))
    self.f_out.write("      load_threshold_variance : {}\n".format(self._load_threshold_variance))
    self.f_out.write("      presample : {}\n".format(self._presample))
    self.f_out.write("      postsample : {}\n".format(self._postsample))
    self.f_out.write("      channel_threshold : true\n")
    self.f_out.write("    }\n")

  def WriteFEM(self,crate,fem):
    if len(self._threshold_map) != 9 or len(self._polarity_map) != 9:
      print "Error: You must run InitThresholdMap() and InitPolarityMap() before generating config! Exiting..."
      exit(1)
    slot = fem + self.GetFirstModule(crate)
    self.f_out.write("    slot{}:{{\n".format(slot))
    self.f_out.write("      bipolar : {}\n".format(self._polarity_map[crate-1][fem]))
    for channel in xrange(self.GetNumberOfChannels(crate,slot)):
      self.f_out.write("      ch{} : {}\n".format(channel,self._threshold_map[crate-1][fem][channel]))
    self.f_out.write("    }\n")

  def CopyUntilString(self,s):
    while True:
      line = self.f_in.readline()
      if line == "":
        print "Error: End of file encountered unexpectedly! Exiting..."
        exit(1)
      self.f_out.write(line)
      if s in line:
        return

  def SyncInputFile(self):
    self.f_out.write("  }\n")
    self.f_out.write("}  ]\n")
    while True:
      line = self.f_in.readline()
      if "}  ]" in line:
        return

  def CopyUntilEnd(self):
    while True:
      line = self.f_in.readline()
      if line == "":
        return
      else:
        self.f_out.write(line)

  def InitThresholdMap(self):
    self._threshold_map = []
    for crate_it in range(1,10):
      crate_thresholds = []
      for fem_it in xrange(self.GetNumberOfModules(crate_it)):
        slot_thresholds = []
        slot = fem_it + self.GetFirstModule(crate_it)
        for channel_it in xrange(self.GetNumberOfChannels(crate_it,slot)):
          slot_thresholds.append(self._threshold)
        crate_thresholds.append(slot_thresholds)
      self._threshold_map.append(crate_thresholds)

  def SetChannelThreshold(self,crate,slot,channel,threshold):
    if len(self._threshold_map) != 9:
      print "Error: Crate number must be a number between 1 and 9! Exiting..."
      exit(1)
    fem = slot - self.GetFirstModule(crate)
    self._threshold_map[crate-1][fem][channel] = threshold

  def InitPolarityMap(self):
    self._polarity_map = []
    for crate_it in range(1,10):
      crate_polarity = []
      for fem_it in xrange(self.GetNumberOfModules(crate_it)):
        if crate_it == 1 or crate_it == 9:
          crate_polarity.append(1)
        else:
          crate_polarity.append(0)
      self._polarity_map.append(crate_polarity)

  def SetPolarity(self,crate,slot,polarity):
    if len(self._polarity_map) != 9:
      print "Error: Must run InitPolarityMap before setting individual polarity! Exiting..."
      exit(1)
    if polarity < 0 or polarity > 2:
      print "Error! Polarity setting must be 0, 1 or 2! Exiting..."
      exit(1)
    fem = slot - self.GetFirstModule(crate)
    self._polarity_map[crate-1][fem] = polarity

  def GetFirstModule(self,crate):
    if crate == 1:
      return 8
    elif crate > 1 and crate < 9:
      return 4
    elif crate == 9:
      return 5
    else:
      print "Error: Crate number must be a number between 1 and 9! Exiting..."
      exit(1)

  def GetNumberOfModules(self,crate):
    if crate == 1:
      return 11
    elif crate > 1 and crate < 9:
      return 15
    elif crate == 9:
      return 14
    else:
      print "Error: Crate number must be a number between 1 and 9! Exiting..."
      exit(1)

  def GetNumberOfChannels(self,crate,slot):
    if crate == 1 and slot == 8:
      return 32
    elif crate == 9 and slot == 5:
      return 32
    else:
      return 64

  def SetLoadThresholdMean(self,load_threshold_mean):
    self._load_threshold_mean = load_threshold_mean

  def SetLoadThresholdVariance(self,load_threshold_variance):
    self._load_threshold_variance = load_threshold_variance

  def SetPresample(self,presample):
    self._presample = presample

  def SetPostsample(self,postsample):
    self._postsample = postsample

  def SetBaseThreshold(self,threshold):
    self._threshold = threshold
