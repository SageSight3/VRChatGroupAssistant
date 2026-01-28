//Simple function to read user input from cmdline
pub fn read_user_input(prompt: &str) -> String {
    use ::std::io::Write;
    print!("{}", prompt);
    ::std::io::stdout().flush().expect("Failed to flush stdout");

    let mut input = String::new();
    ::std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    input.trim().to_string()
}

//Deobfuscates text obfuscated with obfuscate_text()
pub fn deobfuscate_text(obfuscated_text: &String) -> String {
    let mut deobfuscated_text = "".to_string();

    for char in obfuscated_text.chars() {
        deobfuscated_text.push(char::from_u32(char as u32 - 7 as u32).unwrap());
    }

    deobfuscated_text
}

//Obfuscates text for sake of obscuring sensitive data
//IMPORTANT: THIS IS NOT SECURE!!! This function exists purely for the sake
//of wanting to keep sensitive info that needs to be stored in a file from
//being easily read by human observers, or being readable in possible screenshots
//taken without consent by people or software features like Windows Recall
pub fn obfuscate_text(unobfuscated_text: &String) -> String {
    let mut obfuscated_text = "".to_string();

    for char in unobfuscated_text.chars() {
        obfuscated_text.push(char::from_u32(char as u32 + 7 as u32).unwrap());
    }

    obfuscated_text
}