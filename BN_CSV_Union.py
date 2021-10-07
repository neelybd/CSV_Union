from file_handling import *
import sys


def main():
    print("Program: BN_CSV_Union")
    print("Release: 1.1.1")
    print("Date: 2021-10-06")
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

    # Ask for output
    file_out_path = select_file_out_csv(files_in[0])

    # Concatenate variables
    for i in files_in:
        print('Opening File: ' + i)
        concatenated = pd.concat([concatenated, open_unknown_csv(i, delimination)])
        print('File: ' + i + ' opened!')
        print()

    # Export file
    concatenated.to_csv(file_out_path, index=False)

    # CSV's concatenated
    input("CSV's concatenated! Press enter to close...")


if __name__ == '__main__':
    main()
