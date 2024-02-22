//Create a game of higher or lower, where the computer will generate a random
//number between 0 and 100 and the user will try to guess the number.
//If the guessed number is lower than the computers, the computer will say Higher
//If the guessed number is higher than the computers, the computer will say Lower
//If the user guessed the right number, the game ends and user wins
//If the user doesn't get the right number in a specificed number of tries, 
//the computer wins. The user will input how many tries this should take

//Rules: 
//1) The computer random number, user's input, and amount of tries should be 
//   implemented as Macros
//2) Use a True while loop to keep track of the tries and if the maximum amount 
//   of tries is set or the player wins, use break to get out of the loop
//3) Use if statements to compare the user's number against the computer's number

//Extra credit: Let the user choose between two modes: easy and hard ("dark souls")
//The easy mode is just the base game
//In the hard mode, based on the amount of tries the person takes in, increase the 
//range of the numbers. For example, 10 tries means double the range (0 - 200)
//The same base rules apply to both modes