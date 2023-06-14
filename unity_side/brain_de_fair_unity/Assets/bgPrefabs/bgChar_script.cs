using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgChar_script : MonoBehaviour
{

    public float jumpForce;
    private float ySpeed;

    public int activeAnim = 0; 

    public GameObject character;
    
    // Start is called before the first frame update
    void Start() { 
      
    }

    // Update is called once per frame
    void Update() {
        if (activeAnim == 1){
            if (Input.GetKeyDown(KeyCode.Space)){   // θα γίνεται σε random
                // Debug.Log("Playing amin");
                character.GetComponent<Animator>().Play("move");
                // buggarei αν ξεκινήσει animation όσο τρέχει ήδη ένα 
            }           
        }
       
    }

    private void jump(){
        GetComponent<Rigidbody>().AddForce(Vector3.up * jumpForce);
    }
}
