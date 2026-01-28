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

pub fn deobfuscate_text(obfuscated_text: &String) -> String {
    let mut deobfuscated_text = "".to_string();

    for char in obfuscated_text.chars() {
        deobfuscated_text.push(char::from_u32(char as u32 - 7 as u32).unwrap());
    }

    deobfuscated_text
}

pub fn obfuscate_text(unobfuscated_text: &String) -> String {
    let mut obfuscated_text = "".to_string();

    for char in unobfuscated_text.chars() {
        obfuscated_text.push(char::from_u32(char as u32 + 7 as u32).unwrap());
    }

    obfuscated_text
}