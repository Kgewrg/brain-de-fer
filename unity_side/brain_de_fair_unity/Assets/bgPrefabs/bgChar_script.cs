using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgChar_script : MonoBehaviour
{

    public int activeAnim = 0; 
    public float minInterval = 5;
    public float maxInterval = 10;   
    private Animator mAnimator;

    private bool firstStage = true;

    // Start is called before the first frame update
    void Start() { 
        mAnimator = GetComponent<Animator>();
        float randInterval = Random.Range(minInterval, maxInterval);
        Invoke("randomlyInvokeAnim", randInterval);
      
    }

    // Update is called once per frame
    void Update() {
                 
    }

    void randomlyInvokeAnim(){
        // Αυτό καλείτε μια φορά στην αρχή και μετα μάλλον καλείτε απο μόνο του
        // όποτε θέλει ???
        // https://www.youtube.com/watch?v=a76azKiNsYM
        float randInterval = Random.Range(minInterval, maxInterval);
        Invoke("randomlyInvokeAnim", randInterval);
        playAnim();
    }
    
    void playAnim(){
        var state = mAnimator.GetCurrentAnimatorStateInfo(0);
        // Ελέγχει αν είναι active χαρακτήρας και αν παίζει ήδη κάποιο animation
        if ((activeAnim == 1)){
            // Αλλάζει κατάσταση όποτε παίζει animation
            if (firstStage){
                // Παίζει το πρώτο anim, και αλλάζει το flag για να πάει στο δευτερο
                // Debug.Log("playing anim1");
                mAnimator.Play("0", 0);
                firstStage = false;
            }
            else {
                // Αντίστοιχα με το πρώτο
                // Debug.Log("playing anim2");
                mAnimator.Play("1", 0);
                firstStage = true;
            }
        } 
    }
}
