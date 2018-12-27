#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

string one_hot(string seq)
{
    string one_hot_res ="";
    for(int i=0;i<seq.size();i++)
    {
        if(!isalpha(seq[i]))
        {
            cout<<"Not a seq line!"<<endl;
            return one_hot_res;
        }
        string res(26,'0');
        res[seq[i]-'A']='1';
        one_hot_res+=res;
        
    }
    string  one_hot_ress ="";
    for(int i=0;i<one_hot_res.size();i++)
    {
        one_hot_ress+=one_hot_res[i];
        one_hot_ress+=' ';
    }
    return  one_hot_ress;
}


int main()
{
    vector<string> clc_nms;
    ifstream class_names("class_names.txt");
    string line = "";
    while(getline(class_names,line))
    {
        clc_nms.push_back(line);
    }
    class_names.close();
    /*
    ifstream* files = new ifstream[4];
    files[0].open("class1-PDOC00137.fasta");
    ofstream output("whole_dataset.txt");
     */
    
    string mk = ">";
    //string line = "";
    
    
    for(int i=0;i<clc_nms.size();i++)
    {
        ifstream input;
        input.open(clc_nms[i]);
        if(!input.is_open())
        {
            cout<<clc_nms[i]<<endl;
            //exit (-1);
            continue;
        }
        
        ofstream output(clc_nms[i].substr(0,7)+".txt");
        
        
        int cn=0;
        getline(input,line);
    
        while(!input.eof() && !line.empty())
        {
            if(line.find(mk)!=string::npos)
            {
                string reading ="";
                getline(input,line);
                reading+=line;
                getline(input,line);
                while(!line.empty()&&line.find(mk)==string::npos&&!input.eof())
                {
                    reading+=line;
                    getline(input,line);
                }
                if(reading.size()>=400&&reading.size()<=600){
                
                    string one_hot_seq = one_hot(reading.substr(0,400));
                    output<<one_hot_seq;
                    
                    //string family(clc_nms.size(),'0');
                    //family[i]='1';
                    //output<<"   "<<family<<endl;
                    output<<"   "<<i+1<<endl;
                    cn++;
                }
                if(cn>=6000)
                    break;
            }
        }
        cout<<"class"<<i+1<<":"<<cn<<endl;
        input.close();
    }

}
