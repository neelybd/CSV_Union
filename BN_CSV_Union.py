from file_handling import *
import sys


def main():
    print("Program: BN_CSV_Union")
    print("Release: 1.1.0")
    print("Date: 2019-12-11")
    print("Author: Brian Neely")
    print()
    print()
    print("This program reads multiple csv files, will union the data, and export as a csv.")
    print()
    print()

    # Select initial file
    files_in = select_multiple_files("Select multiple files for union", "csv")
    if files_in is None:
        input("No Files Selected. Terminating Program...")
        sys.exit()

    # Ask for file delimination
    delimination = input("Enter File Deliminator: ")

    # Create a blank variable
    concatenated = None

    # Concatenate variables
    for i in files_in:
        concatenated = pd.concat([concatenated, open_unknown_csv(i, delimination)])

    # Export file
    concatenated.to_csv(select_file_out_csv(files_in[0]), index=False)

    # CSV's concatenated
    input("CSV's concatenated! Press enter to close...")


if __name__ == '__main__':
    main()
