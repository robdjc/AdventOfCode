#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

using namespace std;

struct my_data_point
{
    unsigned int min;
    unsigned int max;
    unsigned int start;
};

my_data_point get_mdp(string line)
{
    my_data_point mdp;

    string data_no;
    stringstream ss(line);
    int i = 0;
    while(getline(ss, data_no, ' '))
    {
        if (!data_no.empty())
        {
            // cout << ':' << data_no << ':' << endl;
            switch (i)
            {
                case 0:
                    mdp.start = std::stoul(data_no);
                    break;
                case 1:
                    mdp.min = std::stoul(data_no);
                    break;
                case 2:
                    mdp.max = mdp.min + (std::stoul(data_no) -1);
                    break;
            }
            i++;
        }
    }

    return mdp;
}

void print_mdp(vector<my_data_point> vec_mdps)
{
    for (auto& mdp : vec_mdps)
    {
        cout << "min "   << mdp.min     << ", "
             << "max "   << mdp.max     << ", "
             << "start " << mdp.start   << endl;
    }
}

void add_seeds(const int part, const string& seeds, vector<unsigned int>& vec_seeds)
{
    string seed_no;
    stringstream ss(seeds);

    if(part == 1)
    {
        while(getline(ss, seed_no, ' '))
        {
            if (!seed_no.empty())
            {
                // cout << seed_no << endl;
                vec_seeds.push_back(stoul(seed_no));
            }
        }        
    }
    else
    {
        unsigned int start = 0;

        while(getline(ss, seed_no, ' '))
        {
            if (!seed_no.empty())
            {
                if (start == 0)
                {
                    start = stoul(seed_no);
                }
                else
                {
                    unsigned int max = start + stoul(seed_no);
                    for ( int i = start; i < max; i++ )
                    {
                        vec_seeds.push_back(i);
                    }
                    
                    start = 0;
                }
            }
        }        
    }
}

int crunch_data(const int part)
{
    ifstream infile("input.txt");

    unsigned lowest_location = std::numeric_limits<unsigned>::max();;

    vector<unsigned int> vec_seeds;
    vector<my_data_point> vec_soil_mdps;
    vector<my_data_point> vec_fertilizer_mdps;
    vector<my_data_point> vec_water_mdps;
    vector<my_data_point> vec_light_mdps;
    vector<my_data_point> vec_temperature_mdps;
    vector<my_data_point> vec_humidity_mdps;
    vector<my_data_point> vec_location_mdps;

    string name;
    string line;
    while (getline(infile, line))
    {
        size_t index = line.find_first_of(":");
        if (index != string::npos)
        {
            name = line.substr(0, index);
            string seeds = line.substr(index+1);
            add_seeds(part, seeds, vec_seeds);
        }
        else
        {
            if( line.empty() )
            {
                name.clear();
            }

            if (name == "seed-to-soil map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_soil_mdps.push_back(mdp);
            }
            else if (name == "soil-to-fertilizer map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_fertilizer_mdps.push_back(mdp);
            }
            else if (name == "fertilizer-to-water map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_water_mdps.push_back(mdp);
            }
            else if (name == "water-to-light map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_light_mdps.push_back(mdp);
            }
            else if (name == "light-to-temperature map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_temperature_mdps.push_back(mdp);
            }
            else if (name == "temperature-to-humidity map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_humidity_mdps.push_back(mdp);
            }
            else if (name == "humidity-to-location map" )
            {
                my_data_point mdp = get_mdp(line);
                vec_location_mdps.push_back(mdp);
            }

        }

    }

    unsigned int soil = 0;
    unsigned int fertilizer = 0;
    unsigned int water = 0;
    unsigned int light = 0;
    unsigned int temperature = 0;
    unsigned int humidity = 0; 
    unsigned int location = 0;

    // print_mdp(vec_soil_mdps);
    // print_mdp(vec_fertilizer_mdps);
    // print_mdp(vec_water_mdps);

    for (auto& seed : vec_seeds)
    {
        soil = seed;
        for (auto& mdp : vec_soil_mdps)
        {
            if(seed >= mdp.min && seed <= mdp.max)
            {
                soil = mdp.start + (seed - mdp.min);
            }
        }

        fertilizer = soil;
        for (auto& mdp : vec_fertilizer_mdps)
        {
            if(soil >= mdp.min && soil <= mdp.max)
            {
                fertilizer = mdp.start + (soil - mdp.min);
            }
        }

        water = fertilizer;
        for (auto& mdp : vec_water_mdps)
        {
            if(fertilizer >= mdp.min && fertilizer <= mdp.max)
            {
                water = mdp.start + (fertilizer - mdp.min);
            }
        }

        light = water;
        for (auto& mdp : vec_light_mdps)
        {
            if(water >= mdp.min && water <= mdp.max)
            {
                light = mdp.start + (water - mdp.min);
            }
        }

        temperature = light;
        for (auto& mdp : vec_temperature_mdps)
        {
            if(light >= mdp.min && light <= mdp.max)
            {
                temperature = mdp.start + (light - mdp.min);
            }
        }

        humidity = temperature;
        for (auto& mdp : vec_humidity_mdps)
        {
            if(temperature >= mdp.min && temperature <= mdp.max)
            {
                humidity = mdp.start + (temperature - mdp.min);
            }
        }

        location = humidity;
        for (auto& mdp : vec_location_mdps)
        {
            if(humidity >= mdp.min && humidity <= mdp.max)
            {
                location = mdp.start + (humidity - mdp.min);
            }
        }

        /*
        cout << "Seed "        << seed        << ", "
             << "soil "        << soil        << ", "
             << "fertilizer "  << fertilizer  << ", "
             << "water "       << water       << ", "
             << "light "       << light       << ", "
             << "temperature " << temperature << ", "
             << "humidity "    << humidity    << ", "
             << "location "    << location    << "."  << endl;
        */

        if (location < lowest_location)
        {
            lowest_location = location;
        }
    }

    return lowest_location;
}

unsigned int part2()
{
    unsigned int total = 0;
    return total;
}

int main()
{
    // part1();
    cout << "Part 1: " << crunch_data(1) << endl;

    // took two hours to run :-(
    cout << "Part 2: " << crunch_data(2) << endl;
    return 0;
}