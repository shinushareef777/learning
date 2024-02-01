// use std::io;
// use std::cmp::Ordering;
// use rand::Rng;

// fn main(){
//     println!("Guessing game\n");

//     let secret_number = rand::thread_rng().gen_range(1..=100);

//     let mut count: u32 = 0;

//     loop {
//         println!("Guess a number between 1 and 100");

//         let mut guess = String::new();

//         io::stdin()
//             .read_line(&mut guess)
//             .expect("Failed to read line");

//         let guess: u32 = match guess.trim().parse(){
//             Ok(num) => num,
//             Err(_) => continue
//         };

//         println!("You guessed: {guess}");

//         count += 1;
//         match guess.cmp(&secret_number){
//             Ordering::Less => println!("Too small\n"),
//             Ordering::Greater => println!("Too big\n"),
//             Ordering::Equal => {
//                 println!("You win!\n");
//                 break;
//             }
//         }
//     }

//     println!("You guessed in {count} tries");
// }

// use std::fs::File;
// use std::io::ErrorKind;

// fn main() {
//     let new_file = File::open("hello.txt");
//     let files = match new_file {
//         Ok(file) => file,
//         Err(error) => match error.kind() {
//             ErrorKind::NotFound => match File::create("hello.txt") {
//                 Ok(fc) => fc,
//                 Err(e) => panic!("Problem creating file{:?}", e),
//             },
//             other_error => {
//                 panic!("Problem opening the file: {:?}", other_error);
//             }
//         },
//     };
// }

// use std::fs::File;
// use std::io::{self, Read};

// fn read_username_from_file() -> Result<String, io::Error> {
//     let username_file_result = File::open("hell.txt");

//     let mut username_file = match username_file_result {
//         Ok(file) => file,
//         Err(e) => return Err(e),
//     };

//     let mut username = String::new();

//     match username_file.read_to_string(&mut username) {
//         Ok(_) => Ok(username),
//         Err(e) => Err(e),
//     }
// }


// #[derive(Debug, PartialEq, Copy, Clone)]
// enum ShirtColor {
//     Red,
//     Blue,
// }

// struct Inventory {
//     shirts: Vec<ShirtColor>,
// }

// imple Inventory {
//     fn giveaway(&self, preference: Option<ShirtColor>) -> ShirtColor {
//         preference.unwrap_or_else(|| self.most_stocked())
//     }

//     fn most_stocked(&self) -> ShirtColor {
//         let mut num_red = 0;
//         let mut num_blue = 0;

//         for color in &self.shirts {
//             match color {
//                 ShirtColor::Red => num_red += 1,
//                 ShirtColor::Blue => num_blue += 1,
//             }
//         }

//         if num_red > num_blue {
//            return ShirtColor::Red
//         } else {
//             return ShirtColor::Blue
//         }
//     }
// }

// fn main() {
//     let store = Inventory {
//         shirts: vec![ShirtColor::Blue, ShirtColor::Red, ShirtColor::Blue],
//     };
    
// }

// use std::ops::Deref;

// struct MyBox<T>(T);

// impl<T> MyBox<T> {
//     fn new(x: T) -> MyBox<T> {
//         MyBox(x)
//     }
// }

// impl<T> Deref for MyBox<T> {
//     type Target = T;

//     fn deref(&self) -> &Self::Target {
//         &self.0
//     }

// }


struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(T)
    }
}

fn main() {
    let x = 5;
    // let y = MyBox::new(x);
    // let y = &x;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}


