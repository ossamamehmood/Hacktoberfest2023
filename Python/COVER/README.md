## COVER STEG
```
0.Command Line Steganography Tool  Written in Python
1. Command Line support 
2.Easy to Automate
3.Both Encode and Decode Option
```


❯ Usage :
Encoding : 
`python3 app.py -e <secret text>  <encodedoutput_filename> `

Example :

❯ `python3 app.py  -e 'The-super-secret-forever' secret.txt`

file saved as : secret.txt

content of    secret.txt :

❯ head secret.txt








----



Decoding : 
`python3  app.py -d <encoded-text-file>`

Example :

❯ `python3 app.py -d secret.txt`

The-super-secret-forever

❯ `cat  decoded.txt`

The-super-secret-forever
