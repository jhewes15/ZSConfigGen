
# ZSConfigGen
## Zero suppression configuration generation tool
Written by jhewes15@fnal.gov

ZeroSuppression.py contains the generator class which generates the 
configuration. GenConfig.py is an example script which uses the 
generator to generate a config. To generate a config, you should do 
the following:
```
from ZeroSuppression import ConfigGen
zsgen = ConfigGen([path to imput config],[path to output config])
```
The tool takes an existing config and strips out the existing zero 
suppression configuration, replacing it with the user-defined 
configuration. The remainder of the configuration FHICL remains 
unchanged.

The user can define the following base variables:
```
zsgen.SetLoadThresholdMean([value])
zsgen.SetLoadThresholdVariance([value])
zsgen.SetPresample([value])
zsgen.SetPostsample([value])
zsgen.SetBaseThreshold([value])
```
The function SetBaseThreshold defines a nominal zero suppression 
threshold value which is set as default for all channels. The user 
can then set individual channel thresholds for any channels which 
require a threshold which is greater or smaller than the nominal 
value.

Once the base threshold has been set, the user can initialise maps 
for threshold and polarity.
```
zsgen.InitThresholdMap()
zsgen.InitPolarityMap()
```
After this map has been initialised, the user can now define 
polarity values for specific FEMs, and thresholds for specific 
channels.
```
zsgen.SetChannelThreshold([crate],[slot],[channel],[threshold])
zsgen.SetPolarity([crate],[slot],[polarity])
```
Once the user has defined some configuration of their choosing, 
they can generate a revised configuration file.
```
zsgen.GenConfig()
```
For any questions, comments or complaints, please contact me at 
jhewes15@fnal.gov.
