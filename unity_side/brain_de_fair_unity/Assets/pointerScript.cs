using System.Collections;
using System.Collections.Generic;
using System.IO;

using UnityEngine;

public class pointerScript : MonoBehaviour
{
    Renderer rend;
    public int degrees;
    string filePath;

    void Start(){
        rend = GetComponent<Renderer>();
        rend.material.SetColor("_Color ", Random.ColorHSV());     
        filePath = Application.dataPath + "/value.txt";

    }   

    void Update() {
        
        try{
            string[] lines = File.ReadAllLines(filePath);
            degrees = int.Parse(lines[lines.Length-1]);
            degrees = degrees * -1;  
            // Το αντιστρέφω γιατι κάτι έχω γαμήσει όταν έφτιαξα το sprite και κτλ 
        }
        catch (IOException){
            Debug.Log("File was opened, skipping");
        }

        // degrees = Random.Range(0, 180);
        transform.localEulerAngles =  new Vector3(0, degrees, 0);
        
        // transform.RotateAround(target.position, transform.up, degrees * Time.deltaTime);
        
    }
}
