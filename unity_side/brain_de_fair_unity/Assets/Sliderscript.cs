using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;


public class Sliderscript : MonoBehaviour
{
    public Slider mainslider;
    public LogicScript logic;
    private float player1,starttime,endtime,Finaltime,player2,maxValue;
    private string row,filePath;
    private bool gameover;
    
    // Start is called before the first frame update
    void Start()
    {
       starttime=Time.time;
       gameover=false;
       maxValue=mainslider.maxValue;
       mainslider.value=maxValue/2;
       filePath="C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv";
        // filePath="C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv";//βάλτο σε σχόλιο όταν δεν το χρησιμοποιείς
    }

    // Update is called once per frame
    void Update()
    {
        try{
            string[] lines = File.ReadAllLines(filePath);//χωρίζω το csv σε ενα πίνακα που κάθε στήλη είναι ένας αριθμός(ποσοστό)
            lines=lines[0].Split(',');                  

            player1 = float.Parse(lines[0]);
            player2=float.Parse(lines[1]);
            // Debug.Log("Current value of player1 : "+ player1+" Value of Player2 : "+player2);
            if(gameover == false)
            {
                if( player1 > player2 )
                {
                    mainslider.value=mainslider.value+Time.deltaTime;
                }
                else if(player1 < player2)
                {
                    mainslider.value=mainslider.value-Time.deltaTime;
                }
            }

        
        }
        catch (IOException){
            Debug.Log("File was opened, skipping");
        }
        if( mainslider.value == mainslider.maxValue )
        {
            gameover = logic.GameOverPlayer("Player 1 wins");
            endtime=Time.time;
            Finaltime=starttime-endtime;
            
        }
        else if ( mainslider.value == mainslider.minValue)
        {
            gameover = logic.GameOverPlayer("Player 2 wins");
            endtime=Time.time;
            Finaltime=starttime-endtime;
        }

    }
    
}

