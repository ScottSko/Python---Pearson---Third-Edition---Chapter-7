def main():

    verifier = "n"

    names = ["Sapphire", "Emerald", "Topaz", "Ruby"]

    for string in names:

        if string == "Ruby":
            print("Hello Ruby")
            verifier = "y"

    if verifier == "n":
        print("No Ruby")

main()