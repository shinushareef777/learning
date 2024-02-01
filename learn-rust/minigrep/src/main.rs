use std::env; // crate to accept command line arguments
use std::process;
use minigrep::Config;


fn main() {
  // argument inputs in the command line
  let args: Vec<String> = env::args().collect();
  let config = Config::build(&args).unwrap_or_else(|err| {
    process::exit(1);
  });

  if let Err(e) = minigrep::run(config){
   println!("Application error {e}");
   process::exit(1); 
  }
}


