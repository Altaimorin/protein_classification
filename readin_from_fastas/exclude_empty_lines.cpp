#include<iostream>
#include<fstream>
#include<string>
int classes = 12;

using namespace std;

int main()
{
    for(int i=1;i<classes;i++)
    {
        for(int j=i+1;j<=classes;j++)
        {
            string train_input = "class"+to_string(i)+"_"+to_string(j)+"_train.txt";
            string test_input = "class"+to_string(i)+"_"+to_string(j)+"_test.txt";
            
            string new_train_input = "new_"+train_input;
            string new_test_input = "new_"+test_input;
            
            ifstream input1(train_input);
            ifstream input2(test_input);
            ofstream output1(new_train_input);
            ofstream output2(new_test_input);
            
            string line = "";
    
            int cn =0;
            while(!input1.eof())
            {
                getline(input1,line);
                cn++;
                /*
                if(line.empty())
                {
                    cout<<train_input<<endl;
                    cout<<"test: cn = "<<cn<<endl;
                }*/
                if(!line.empty())
                    output1<<line<<endl;
            }
    
            line="";
            cn = 0;
            while(!input2.eof())
            {
                getline(input2,line);
                cn++;
                /*
                if(line.empty())
                {
                    cout<<test_input<<endl;
                    cout<<"train: cn = "<<cn<<endl;
                }
                 */
                if(!line.empty())
                    output2<<line<<endl;
            }
            input1.close();
            input2.close();
            output1.close();
            output2.close();
        }
    }

}
