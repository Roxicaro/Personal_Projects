def main(sequence='', bracket_type=''):
    
  
    print('\nReverse Complement Tool')       
    sequence = input('Input your sequence: ')

    #Dictionary with convertion key
    aminoacid_complement = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    
    #Check if Aminoacid sequence if valid
    valid = ['A', 'T', 'C', 'G']
    for aa in sequence:
        if aa not in valid:
            return print('Invalid aminoacid!')
    
    #Create complement
    complement = []
    for aa in sequence:
        complement.append(aminoacid_complement[aa])
    
    #Reverse complement
    reverse_complement = ''.join(complement[::-1])
    
    return print(f"\nInput: {sequence}\nReverse complement: {reverse_complement}")
       
main()