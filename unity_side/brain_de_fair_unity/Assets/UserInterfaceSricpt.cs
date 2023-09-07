using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class UserInterfaceSricpt : MonoBehaviour
{
    public static int P1_EggConStatus;
    public static int P2_EggConStatus;
    public GameObject conStatusMessage_container;
    // public TMP_Text P2_EGG_text;

    public TMP_Text rightP_TextBox;

    public Slider LeftPlayerHealth;
    public Slider RightPlayerHealth;

    private float sliderValue;

    void Start() {
        conStatusMessage_container.SetActive(false);

        

    }

    void Update() {

        // Αν δεν έχει συνδεθεί η συσκευή, εμφανίζει το text
        if (P1_EggConStatus == 0){
            conStatusMessage_container.SetActive(true);
        }else{
            conStatusMessage_container.SetActive(false);

        }

        // Gia 2 paixtes
        // if ((P1_EggConStatus == 0) || P2_EggConStatus == 0){
        //     P1_EGG_obj.SetActive(true);
        // }else{
        //     P1_EGG_obj.SetActive(false);

        // }


        if (PlayerPrefs.GetInt("gameMode", -1) == 1){
            rightP_TextBox.SetText("Bot's health");
        }
        else {
            rightP_TextBox.SetText("right player's health");
        }

        sliderValue = Sliderscript.publicSliderValue - 5;
        LeftPlayerHealth.value = Remap(sliderValue, 0, -5, 0, 1);
        RightPlayerHealth.value = Remap(sliderValue, 0, 5, 0, 1); 




                      
    }

    float Remap (float value, float from1, float to1, float from2, float to2) {
        return (value - from1) / (to1 - from1) * (to2 - from2) + from2;
    }
}
