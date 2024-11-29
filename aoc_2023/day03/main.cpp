#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <utility>

using namespace std;

int part1()
{
    int total = 0;

    ifstream infile("input.txt");

    // put all data in a vector
    vector<string> my_data;
    string line;
    while (getline(infile, line))
    {
        my_data.push_back(line);
    }

    struct my_data_point
    {
        int line_number;
        int number;
        int position;
        int lenght;
    };

    vector<my_data_point> vec_mdps;

    // loop thru the vector
    int line_number = 0;
    for (auto& vline : my_data)
    {
        // cout << vline << endl;

        bool word = false;
        string my_number;
        int position = 0;
        for (char& c : vline)
        {
            if (isdigit(c))
            {
                word = true;
                my_number += c;
            }
            else
            {
                if(word)
                {
                    word = false;
                    // cout << my_number << endl;

                    my_data_point mdp;
                    mdp.line_number = line_number;
                    mdp.number = stoi(my_number);
                    mdp.position = position - my_number.length(); // hacky
                    mdp.lenght = my_number.length();
                    vec_mdps.push_back(mdp);

                    my_number.clear();
                }
            }

            position++;
            // catch the last one
            if(word && position == vline.length())
            {
                word = false;
                // cout << my_number << endl;

                my_data_point mdp;
                mdp.line_number = line_number;
                mdp.number = stoi(my_number);
                mdp.position = position - my_number.length(); // hacky
                mdp.lenght = my_number.length();
                vec_mdps.push_back(mdp);

                my_number.clear();
            }
        }
        line_number++;
        // break;
    }

    // print out the info
    for (auto& mdp : vec_mdps)
    {
        // cout << "line_number " << mdp.line_number << endl;
        // cout << "number      " << mdp.number << endl;
        // cout << "position    " << mdp.position << endl;
        // cout << "lenght      " << mdp.lenght << endl;
    }

    for (auto& mdp : vec_mdps)
    {
        // cout << "number      " << mdp.number << endl;
        // cout << my_data[mdp.line_number] << endl;

        int left = mdp.position;
        if (left > 0)
        {
            left -= 1;
        }

        int right = mdp.position + mdp.lenght;
        if (right > (my_data[mdp.line_number].length() - 1))
        {
            right -= 1;
        }

        int top = mdp.line_number;
        {
            if (top > 0)
            {
                top -= 1;
            }
        }

        int bottom = mdp.line_number;
        if (bottom < (my_data.size() - 1))
        {
            bottom += 1;
        }

        // cout << "left   " << left   << endl;
        // cout << "right  " << right  << endl;
        // cout << "top    " << top    << endl;
        // cout << "bottom " << bottom << endl;

        for(int i = top; i <= bottom; ++i)
        {
            for(int j = left; j <= right; ++j)
            {
                char c = my_data[i][j];
                // cout << c << endl;
                if(!isdigit(c) && c != '.')
                {
                    // cout << "line " << (mdp.line_number + 1) << ", adding: " << mdp.number << endl;
                    total += mdp.number;
                    continue;
                }
            }
        }

        // break;

    }

    return total;
}

int part2()
{
    int total = 0;

    ifstream infile("input.txt");

    // put all data in a vector
    vector<string> my_data;
    string line;
    while (getline(infile, line))
    {
        my_data.push_back(line);
    }

    struct my_data_point
    {
        int line_number;
        int number;
        int position;
        int lenght;
    };

    vector<my_data_point> vec_mdps;

    // loop thru the vector
    int line_number = 0;
    for (auto& vline : my_data)
    {
        // cout << vline << endl;

        bool word = false;
        string my_number;
        int position = 0;
        for (char& c : vline)
        {
            if (isdigit(c))
            {
                word = true;
                my_number += c;
            }
            else
            {
                if(word)
                {
                    word = false;
                    // cout << my_number << endl;

                    my_data_point mdp;
                    mdp.line_number = line_number;
                    mdp.number = stoi(my_number);
                    mdp.position = position - my_number.length(); // hacky
                    mdp.lenght = my_number.length();
                    vec_mdps.push_back(mdp);

                    my_number.clear();
                }
            }

            position++;
            // catch the last one
            if(word && position == vline.length())
            {
                word = false;
                // cout << my_number << endl;

                my_data_point mdp;
                mdp.line_number = line_number;
                mdp.number = stoi(my_number);
                mdp.position = position - my_number.length(); // hacky
                mdp.lenght = my_number.length();
                vec_mdps.push_back(mdp);

                my_number.clear();
            }
        }
        line_number++;
        // break;
    }

    // print out the info
    for (auto& mdp : vec_mdps)
    {
        // cout << "line_number " << mdp.line_number << endl;
        // cout << "number      " << mdp.number << endl;
        // cout << "position    " << mdp.position << endl;
        // cout << "lenght      " << mdp.lenght << endl;
    }

    map<string, vector<int> > adj_info;

    for (auto& mdp : vec_mdps)
    {
        // cout << "number      " << mdp.number << endl;
        // cout << my_data[mdp.line_number] << endl;

        int star_line_number = mdp.line_number;

        int left = mdp.position;
        if (left > 0)
        {
            left -= 1;
        }

        int right = mdp.position + mdp.lenght;
        if (right > (my_data[mdp.line_number].length() - 1))
        {
            right -= 1;
        }

        int top = mdp.line_number;
        {
            if (top > 0)
            {
                top -= 1;
                star_line_number -= 1;
            }
        }

        int bottom = mdp.line_number;
        if (bottom < (my_data.size() - 1))
        {
            bottom += 1;
        }

        // cout << "left   " << left   << endl;
        // cout << "right  " << right  << endl;
        // cout << "top    " << top    << endl;
        // cout << "bottom " << bottom << endl;

        for(int i = top; i <= bottom; ++i)
        {
            for(int j = left; j <= right; ++j)
            {
                char c = my_data[i][j];
                // cout << c << endl;
                if(c == '*')
                {
                    // cout << "star adjascent number " << mdp.number << endl;
                    // cout << "mdp.line_number  " << mdp.line_number << endl;
                    // cout << "star_line_number " << star_line_number << endl;
                    // cout << "i " << i << endl;
                    // cout << "pos j " << j << endl;

                    stringstream skey;
                    skey << "L" << star_line_number << "P" << j << "X";
                    // cout << skey.str() << endl;
                    
                    if (adj_info.count(skey.str()))
                    {
                        adj_info[skey.str()].push_back(mdp.number);
                    } else
                    {
                        adj_info.insert(pair<string,vector<int> >(skey.str(), vector<int>()));
                        adj_info[skey.str()].push_back(mdp.number);
                    }
                }
            }
            star_line_number++;
        }

        // break;

    }

    for (auto& x : adj_info)
    {
        if (x.second.size() == 2)
        {
            // std::cout << x.first  // string (key)
            //         << ':' 
            //         << x.second.size() // string's value 
            //         << std::endl;
            int temp_total = 1;
            for (auto& numx : x.second)
            {
                temp_total *= numx;
            }
            total += temp_total;
        }
    }

    return total;
}

int main()
{
    // your answer is too low 538237
    // Part 1: 539637

    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
    // part1();
    // part2();
    return 0;
}