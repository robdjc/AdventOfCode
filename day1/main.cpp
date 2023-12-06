#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int part1()
{
    ifstream infile("input.txt");

    int total = 0;

    string line;
    while (getline(infile, line))
    {
        size_t last_index = line.find_first_of("0123456789");
        string side_left = line.substr(last_index, 1);

        last_index = line.find_last_of("0123456789");
        string side_right = line.substr(last_index, 1);

        string final = side_left + side_right;
        total += std::stoi( final );
    }

    return total;
}

int part2()
{
    
    std::map<string, string> my_numbers
    { 
        {"one",   "1"}, 
        {"two",   "2"}, 
        {"three", "3"},
        {"four",  "4"},
        {"five",  "5"},
        {"six",   "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine",  "9"}
    };

    ifstream infile("input.txt");

    int total = 0;

    string line;
    while (getline(infile, line))
    {
        // Part 2
        std::vector<std::string> stringVec = 
            {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        // check the left most index by number
        size_t left_index = line.find_first_of("0123456789");
        string left_side = line.substr(left_index, 1);

        // check the left most index by name
        for (auto & element : stringVec)
        {
            size_t left_index_s = line.find(element);

            if(left_index_s != string::npos)
            {
                if(left_index_s < left_index)
                {
                    left_index = left_index_s;
                    left_side = my_numbers[element];
                }
            }
        }

        size_t right_index = line.find_last_of("0123456789");
        string right_side = line.substr(right_index, 1);

        // check the right most index by name
        for (auto & element : stringVec)
        {
            size_t right_index_s = line.rfind(element);

            if(right_index_s != string::npos)
            {
                if(right_index_s > right_index)
                {
                    right_index = right_index_s;
                    right_side = my_numbers[element];
                }
            }

        }

        // combine number and add to total
        string final = left_side + right_side;
        total += std::stoi( final );
        // cout << "sum " << total << " " << left_side << " " << 
        //     right_side << endl;
    }

    return total;
}

int main()
{
    // Part 1: 55971
    // Part 2: 54719
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
    return 0;
}