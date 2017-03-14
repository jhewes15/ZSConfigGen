
# ZSConfigGen
## Zero suppression configuration generation tool
Written by jhewes15@fnal.gov

ZeroSuppression.py contains the generator class which generates the 
configuration; it should be imported by a separate Python script in
the same directory. GenConfig.py is an example script which uses the 
generator to generate a config.

The generator takes an existing run configuration FHICL as an input,
then strips out the existing zero suppression configuration and
replaces it with a new configuration according to the user's desired
settings, writing the output to a new FHICL file. To generate a
config, you should do the following:
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
zsgen.SetBasePolarity([value])
```
The functions SetBaseThreshold and SetBasePolarity define a nominal
zero suppression threshold and polarity option which is set as
default for all channels. The user can then set individual channel
thresholds for any channels which differ from the nominal value.

Once the base threshold has been set, the user can initialise maps 
for threshold and polarity.
```
zsgen.InitThresholdMap()
zsgen.InitPolarityMap()
```
After this map has been initialised, the user can now define 
polarity values and thresholds for specific channels.
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
