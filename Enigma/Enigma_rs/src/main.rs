use rand::seq::SliceRandom;
use rand::thread_rng;
use std::io::Read;
use std::io::Write;

#[derive(Debug, Copy, Clone)]

struct Rotor {
    order: [i32; 25],
    cursor: usize,
}

impl Rotor {
    fn turn(&mut self) {
        self.cursor = (self.cursor + 1) % self.order.len();
    }
}

fn encipher_and_decipher(
    ch: char,
    alphabet_slice: &'static str,
    order: [i32; 25],
    cursor: usize,
    sign: i32,
) -> char {
    //println!("ch: {}", ch);
    let pos: i32 = alphabet_slice.find(ch).unwrap() as i32;
    //println!("pos: {}", pos);
    let index_change: i32 = order[cursor] * sign;
    let pos_new: i32 =
        (pos + index_change + alphabet_slice.len() as i32) % alphabet_slice.len() as i32;
    //println!("pos_new: {}", pos_new);

    let ch_new: char = alphabet_slice.chars().nth(pos_new as usize).unwrap();
    //println!("ch_new: {}", ch_new);
    ch_new
}

fn reflect(ch: char, alphabet_slice: &'static str, reflection: [i32; 26]) -> char {
    let index_orig = alphabet_slice.find(ch).unwrap() + 1;
    //println!("index_orig: {}", index_orig);

    let index_new = reflection[(index_orig + (reflection.len() / 2)) % reflection.len()] - 1;
    //println!("index_new: {}", index_new);
    let ch: char = alphabet_slice.chars().nth(index_new as usize).unwrap();
    //println!("ch: {}", ch);
    ch
}

fn rotor_linker(rotor_list: &mut [Rotor; 3], rotors_num: usize, idx: usize) {
    //println!("{}", rotor_list[idx].cursor);
    rotor_list[idx].turn();
    //println!("Rotor[{}] Move!", idx);
    //println!("{}", rotor_list[idx].cursor);
    if rotor_list[idx].cursor == 0 && idx < (rotors_num - 1) {
        rotor_linker(rotor_list, rotors_num, idx + 1)
    }
}

fn main() {
    println!("Enigma Start!");

    let mut my_cypher = String::new();

    let alphabet_slice: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    const rotors_num: usize = 3;
    let mut order_init: [i32; 25] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
    ];
    let cursor_init: usize = 0;

    let mut rotor_list: [Rotor; rotors_num] = [Rotor {
        order: order_init,
        cursor: cursor_init,
    }; rotors_num];

    let password_from = 'm';
    let passwords_file = String::from("passwords.txt");
    // const password_len: usize = 25;

    let reflection_from = 'm';
    let reflection_file = String::from("reflection.txt");
    let reflection_init: [i32; 26] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26,
    ];
    let mut reflection_unit = reflection_init;

    let input_file = String::from("inputFile.txt");
    let output_file = String::from("outputFile.txt");

    if password_from == 'm' {
        for i in 0..rotors_num {
            let mut rng = thread_rng();
            order_init.shuffle(&mut rng);
            rotor_list[i as usize].order = order_init;
        }
    }
    println!("{:?}", rotor_list);

    // get reflection
    if reflection_from == 'm' {
        let mut rng = thread_rng();
        reflection_unit.shuffle(&mut rng);
    }
    println!("reflection_unit: {:?}", reflection_unit);

    // read plain text
    let mut file = std::fs::File::open(input_file).unwrap();
    let mut my_string = String::new();
    file.read_to_string(&mut my_string).unwrap();
    //println!("{}", my_string);
    my_string = String::from(my_string);
    let my_string_trim = my_string.trim();
    let my_string_len = my_string_trim.len();
    //println!("string length: {}", my_string_len);

    // encipher and decipher
    for mut b in my_string_trim.chars() {
        for r in 0..rotors_num {
            b = encipher_and_decipher(
                b,
                alphabet_slice,
                rotor_list[r].order,
                rotor_list[r].cursor,
                1,
            );
        }
        b = reflect(b, alphabet_slice, reflection_unit);
        for r in 0..rotors_num {
            b = encipher_and_decipher(
                b as char,
                alphabet_slice,
                rotor_list[r].order,
                rotor_list[r].cursor,
                -1,
            );
        }
        my_cypher.push(b);
        rotor_linker(&mut rotor_list, rotors_num, 0);
    }

    // save cipher text
    let mut file = std::fs::File::create(output_file).expect("create failed");
    file.write_all(my_cypher.as_bytes()).expect("write failed");
}
