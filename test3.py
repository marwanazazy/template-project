import time
import random

# List of potential names for the character
names = ["Tommy", "Chris", "Ahmed", "Kevin", "David"]
character_name = random.choice(names)



def invalid_input_handler(prompt, valid_options):
    """Prompt the user until they enter a valid option.

    Args:
        prompt (str): The input prompt to show the user.
        valid_options (list): A list of valid options.

    Returns:
        str: The valid user input.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid input. Please enter one of the following: "
                  f"{', '.join(valid_options)}")


def print_delay(message, pause=2):
    """Prints a message and then pauses for a given duration.

    Args:
        message (str): The message to print.
        pause (int): The duration to wait after printing the message.
    """
    print(message)
    time.sleep(pause)


def scoring_system(score):
    """Determine the ending of the story based on the score.

    Args:
        score (int): The total score.

    Returns:
        str: The ending message.
    """
    if score >= 20:
        return (f"Congratulations! You helped {character_name} "
                f"navigate the woods successfully.")
    elif score <= 15:
        return (f"{character_name} made it back home with some scratches, "
                f"but learned valuable lessons.")
    else:
        return (f"Unfortunately, {character_name} didn't make it back home "
                f"safely. Better luck next time!")


def adventure_story(turns):
    """Runs the interactive adventure story where the player makes choices
    for the character and earns a score based on the outcomes of those
    choices.

    Args:
        turns (int): The current number of turns taken.
    """

    character_weapon = ["sword", "broom", "knife"]
    weapon = random.choice(character_weapon)
    print((f"{character_name} was an adventurous boy who loved exploring "
           f"the woods near his home. One sunny afternoon, he ventured deeper "
           f"into the forest than ever before. The trees grew thicker, and soon "
           f"he realized he had lost his way. As the daylight began to fade, "
           f"{character_name} stumbled upon an old, abandoned cabin. He had two "
           f"choices: Enter the Cabin: {character_name} could go inside the cabin "
           f"and search for help or supplies. Continue Walking: {character_name} "
           f"could keep walking in the hope of finding his way back home before "
           f"it got too dark."))
    print_delay(f"What should {character_name} do?")
    print_delay("1. Enter the cabin")
    print("2. Continue walking")

    choice = invalid_input_handler("Enter choice (1/2): ", ["1", "2"])
    turns += 1  # Increment turn counter

    if choice == "1":
        score += 10
        print_delay((f"{character_name} pushed open the creaky door of the cabin "
                     f"and stepped inside. The air was musty, and the furniture "
                     f"was covered in dust. As he searched the room, he found a "
                     "map on a table. The map showed a path leading out of the "
                     "woods. Relieved, {character_name} pocketed the map and "
                     f"turned to leave, but a rustling noise stopped him in his "
                     f"tracks. A wild animal, a raccoon, leaped at {character_name}, "
                     f"baring its teeth. {character_name} had two choices for how "
                     f"to defend himself: 1. Use the Broom: {character_name} could "
                     f"grab the nearby broom and use it to fight off the raccoon. "
                     f"2. Throw a Blanket: {character_name} could grab an old blanket "
                     f"from the couch and use it to shield himself from the raccoon."))
        choice = invalid_input_handler("Enter choice (1/2): ", ["1", "2"])

        if choice == "1":
            score += 10
            print_delay((f"{character_name} grabbed the broom and swung it at the "
                         f"raccoon. The raccoon hissed and ran away. {character_name}, "
                         f"still holding the broom, quickly left the cabin and followed "
                         f"the map's directions. After some time, he finally found his "
                         f"way back home. His parents were relieved and praised him for "
                         f"his bravery."))
        elif choice == "2":
            score += 5
            print_delay((f"{character_name} threw the blanket over the raccoon, "
                         f"confusing it for a moment. He took this chance to escape the "
                         f"cabin. With the map in hand, he navigated through the woods "
                         f"and eventually found his way back home. His parents were "
                         f"worried but glad to see him safe."))
    elif choice == "2":
        score += 5
        print_delay((f"{character_name} decided to keep walking, relying on his "
                     f"instincts to guide him. As the night grew darker, he heard the "
                     f"howls of distant wolves. Fear gripped him, but he pressed on. "
                     f"Suddenly, he heard a growl close by and saw a pair of glowing "
                     f"eyes in the darkness. A wild dog lunged at him. {character_name} "
                     f"had two choices for how to defend himself: 1. Use a Sturdy Stick: "
                     f"{character_name} could grab a sturdy stick from the ground and "
                     f"use it to fight off the wild dog. 2. Climb a Tree: {character_name} "
                     f"could try to climb a nearby tree to escape the wild dog."))
        choice = invalid_input_handler("Enter choice (1/2): ", ["1", "2"])

        if choice == "1":
            score += 10
            print_delay((f"{character_name} quickly grabbed a {weapon} from the ground "
                         f"and faced the wild dog. With courage and determination, he "
                         f"fought off the dog, finally managing to drive it away. "
                         f"Exhausted but triumphant, {character_name} saw the flickering "
                         f"light of a lantern in the distance. It was his father, who had "
                         f"come searching for him. They hugged tightly, and {character_name} "
                         f"vowed never to wander off so far again."))
        elif choice == "2":
            score += 5
            print_delay((f"{character_name} ran to a nearby tree and started climbing "
                         f"as fast as he could. The wild dog jumped and barked at the base "
                         f"of the tree but couldn't reach him. {character_name} waited until "
                         f"the dog lost interest and wandered away. However, he lost his balance "
                         f"while climbing down and fell, injuring his leg. He was found the next "
                         f"morning by his worried parents."))

    return turns



def play_game(turn_limit=5):
    """Main game loop that limits the number of turns.

    Args:
        turn_limit (int): The maximum number of turns the player can take.
    """
    global score
    global turns
    score = 0  # Initialize score
    turns = 0

    while turns < turn_limit:
        turns = adventure_story(turns)
        # Display current score and turns
        print(f"Score: {score}, Turns: {turns}")

        # Check if game over conditions are met
        if score >= 25:
            print("Game Over! You won!")
            return

        # Ask if the player wants to continue, but only if the turn limit is not reached
        if turns < turn_limit:
            continue_game = invalid_input_handler("Do you want to continue? (yes/no): ", ["yes", "no"])   
            if continue_game != "yes":
                break            
        elif turns >= turn_limit:
            break   

    # If the turn limit is reached or the player chooses to stop, end the game
    ending_message = scoring_system(score)
    print(ending_message)


# Example usage
while turns <= 3 :
    if score > 25 :
        break
    play_game(turn_limit=3)
    play_again = invalid_input_handler("Play again? (yes/no): ", ["yes", "no"])
    if play_again != "yes":
        print("Thanks for playing!")
        break
