def main():
    try:
        with open("input.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]

            print("Bilangan yang dibaca dari file input.txt:", numbers)
            
            total = sum(numbers)
            
            formatted_total = "{:,.3f}".format(total)
            
            print("Jumlah bilangan dengan pemisah koma dan format tiga digit:", formatted_total)
    except FileNotFoundError:
        
        print("File tidak ditemukan.")
    except ValueError:
        
        print("File tidak berisi bilangan bulat.")

if __name__ == "__main__":
    main()
