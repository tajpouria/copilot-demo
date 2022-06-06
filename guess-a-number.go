// Generate a random number between 1 and 100.
// Prompt the user to guess the number.
// If the user guesses the number, display a message saying "You guessed the number!"
// If the user guesses a number less than the random number, display a message saying "Your guess is too low."
// If the user guesses a number greater than the random number, display a message saying "Your guess is too high."
// After the user guesses the number, ask if the user wants to play again.
// If the user answers "yes", restart the game.
// If the user answers "no", display a message saying "Thanks for playing!"
// If the user answers something other than "yes" or "no", display a message saying "Please type either yes or no."
// If the user does not answer after three tries, display a message saying "Sorry, you didn't guess the number."

package main

import ( "fmt"
		 "math/rand"
)

func main() {
	// your code goes here
	random_number := rand.Intn(100)
	var guess int
	for i := 0; i < 3; i++ {
		fmt.Println("Guess a number between 1 and 100:")
		fmt.Scanln(&guess)
		if guess == random_number {
			fmt.Println("You guessed the number!")
			break
		} else if guess < random_number {
			fmt.Println("Your guess is too low.")
		} else {
			fmt.Println("Your guess is too high.")
		}
	}
	fmt.Println("Do you want to play again?")
	var answer string
	fmt.Scanln(&answer)
	if answer == "yes" {
		main()
	}
	if answer == "no" {
		fmt.Println("Thanks for playing!")
	} else {
		fmt.Println("Please type either yes or no.")
	}
}