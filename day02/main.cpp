#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

int part1()
{
    std::map<string, int> max_colors
    { 
        {"red",   12}, 
        {"green", 13}, 
        {"blue",  14},
    };

    ifstream infile("input.txt");

    int total = 0;

    set<int> good_game_ids;

    string line;
    while (getline(infile, line))
    {
        size_t space_index = line.find(" ");
        size_t colon_index = line.find(": ");
        string game_number = line.substr(space_index + 1, (colon_index - 1) - space_index);

        vector<string> game_info;

        string segment1;
        string segment2;
        string segment3;

        bool bad_game = false;

        stringstream game_line1(line.substr(colon_index + 2));
        while(getline(game_line1, segment1, ';'))
        {
            stringstream game_line2(segment1);
            while(getline(game_line2, segment2, ','))
            {
                stringstream game_line3(segment2);
                while(getline(game_line3, segment3, ' '))
                {
                    segment3.erase(std::remove(segment3.begin(), segment3.end(), ' '), segment3.end());
                    if(!segment3.empty())
                    {
                        game_info.push_back(segment3);
                    }
                }

                int color_count = std::stoi( game_info[0] );
                if (color_count >  max_colors[game_info[1]])
                {
                    bad_game = true;
                }
                game_info.clear();
            }
        }

        if (!bad_game)
        {
            good_game_ids.insert(std::stoi(game_number));
        }
    }

    // 2888 too high
    for (auto& n : good_game_ids)
    {
        // cout << n << endl;
        total += n;
    }

    return total;
}

int part2()
{
    std::map<string, int> max_colors
    { 
        {"red",   0}, 
        {"green", 0}, 
        {"blue",  0},
    };

    ifstream infile("input.txt");

    int total = 0;

    string line;
    while (getline(infile, line))
    {
        // game line level
        size_t colon_index = line.find(": ");

        vector<string> game_info;

        string segment1;
        string segment2;
        string segment3;

        stringstream game_line1(line.substr(colon_index + 2));
        while(getline(game_line1, segment1, ';'))
        {
            // game level
            stringstream game_line2(segment1);
            while(getline(game_line2, segment2, ','))
            {
                // color level
                stringstream game_line3(segment2);
                while(getline(game_line3, segment3, ' '))
                {
                    segment3.erase(std::remove(segment3.begin(), segment3.end(), ' '), segment3.end());
                    if(!segment3.empty())
                    {
                        game_info.push_back(segment3);
                    }
                }

                string color = game_info[1];
                int color_count = std::stoi( game_info[0] );

                if(color_count > max_colors[color])
                {
                    max_colors[color] = color_count;
                }

                game_info.clear();

            }
        }

        int sub_total = 1;
        for(const auto& elem : max_colors)
        {
            // cout << elem.first << " " << elem.second << " " << endl;
            sub_total *=  elem.second;
        }

        cout << sub_total << endl;

        total += sub_total; 
        max_colors["green"] = 0;
        max_colors["red"] = 0;
        max_colors["blue"] = 0;
    }

    // 2888 too high
    // for (auto& n : good_game_ids)
    // {
    //     // cout << n << endl;
    //     total += n;
    // }
    cout << total << endl;

    return total;
}

int main()
{
    // 2162
    // cout << "Part 1: " << part1() << endl;
    // cout << "Part 2: " << part2() << endl;
    part2();
    return 0;
}