use std::fs;

fn simple_depth_measurement(_contents: &str) {
    // initializes mutable variables to use in for loop
    let mut counter = 0;
    let mut buf: i32 = _contents.lines().nth(0).unwrap().parse::<i32>().unwrap();

    // iterates line for line in file
    for line in _contents.lines() {
        let current = line.trim().parse::<i32>().unwrap();
        let before = buf;

        // checks if previous number is smaller than the current one
        // if so increase counter as depth increases
        if before < current {
            counter += 1;
        }
        buf = current;
    }
    print!("Depth measurement increases {} times.\n", counter);
}

fn sliding_window_measurement(_contents: &str) {
    //let mut counter = 0;
    //let mut sum: [i32; 3] = _contents.lines().nth(0).unwrap().parse::<i32>().unwrap();
//
    //// iterates line for line in file
    //for line in _contents.lines() {
    //    let current = line.trim().parse::<i32>().unwrap();
    //    let before = buf;
//
    //    // checks if previous number is smaller than the current one
    //    // if so increase counter as depth increases
    //    if before < current {
    //        counter += 1;
    //    }
    //    buf = current;
    //}
//
    //print!("Three measurement sliding window increases {} times.\n", counter);
}

fn main() {
    // reads file contents to string
    let filename = "../../../../input/01";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong while reading the file");

    simple_depth_measurement(&contents);
    sliding_window_measurement(&contents);
}
