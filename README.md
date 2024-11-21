# ESP8266_RNG
Tinny random number generate running on ESP8266.

## Introduction:
In the spirit of the RP2040 generator [Link](https://github.com/MicroControleurMonde/RP2040-RNG), the code has been adapted to run on ESP8266EX.

*`Just for fun as proof of concept`.*
## Concept:

A Micro-python library which provides an interface to generate a random number using the ESP8266's capabilities. 

It enables Wi-Fi temporarily to enhance entropic noise, reads a random value from the ADC, and then disables Wi-Fi.

- Library : **esp8266_rng_lib**
- Libarary test: **Test_Simple_ESP8266_rng_lib.py**
- Example (100'000 values): **esp8266_100000.py**

The random number generated by the library is **64 bits**.

## Performance:

- Elapsed Time to generate 100000 values: 14 minutes and 11 secondes (**851  sec.**)
- Throughput: **942 Bytes/sec**
- **117** random values / sec.

## RNG testing

For verification purposes, we will only run Ent tests to quantify and assess the quality of the numbers generated.

### Ent Test

[Ent](https://www.fourmilab.ch) John Walker

- Sample size: 1.94 MB (in the Ent Folder)
- Total generated: 100'000 values
- [Ent report - Raw](https://github.com/MicroControleurMonde/ESP8266_RNG/blob/main/Ent/Ent_report.txt)

### Ent Analysis :

- **Entropy**: **3.44 bits per byte**, which shows that the data generated is not perfectly random.
- **Compression**: The data is 57% compressible, indicating a certain amount of redundancy.
- **Distribution**: The distribution of values is broadly uniform, but the entropy and Pi calculations show that there are still biases in the data.
- **Correlation**: The data is almost uncorrelated, which is good for randomness.

## Conclusion:
So, overall the generator produces random numbers with good quality, but there are biases.

On the downside, the generator is extremely slow ... which is normal for this kind of small MCU.
