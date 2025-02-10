if ARGV.length != 1
    puts "Veuillez vérifier le nombre d'arguments passés ! Il doit y en avoir un seul."
    exit
  end
  
  argument = ARGV[0].downcase
  alphabet = ('a'..'z').to_a
  

  unless alphabet.include?(argument)
    puts "L'argument doit être une lettre de l'alphabet !"
    exit
  end
  
 
  indice_argument = alphabet.index(argument)
  puts alphabet[indice_argument..-1].join