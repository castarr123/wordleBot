# wordleBot
Basic bot for solving Wordle


To add a guess to the bot edit the guesses[]
1 = not in the word
2 = in the word in the wrong place 
3 = in the correct place 

for example 
guesses = [guess("toeas","11222"),guess("saree","32213")]
first it would use toeas, with T and O being not in the word and E A S being in the word but in the wrong spots 
then it would use saree, with S and E in the correct spots, A and R in the wrong spot and a second E not in the word

when run it will console log the best next guess, if it logs Sneed that means there is an error and for some reason it is eliminating all words
