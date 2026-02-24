use serde_json;
use ::std::io::{stdin, stdout, Write};
use std::fs::read_to_string;

//Simple function to read user input from cmdline
pub fn read_user_input(prompt: &str) -> String {
    print!("{}", prompt);
    stdout().flush().expect("Failed to flush stdout");

    let mut input = String::new();
    stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    input.trim().to_string()
}

//Return parsed json data from a file
pub fn parse_json(json_file_path: &str) -> serde_json::Value {
    //https://doc.rust-lang.org/std/fs/fn.read_to_string.html
    let file = read_to_string(json_file_path)
        .expect(format!("Failed to open JSON file: {}", json_file_path).as_str());
    
    let json: serde_json::Value = serde_json::from_str(file.as_str())
        .expect(format!("Failed to parse JSON file: {}", json_file_path).as_str());

    json
}