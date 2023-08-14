using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{

    public GameObject[] charPrefab_array;
    public GameObject centerPoint; 

    [Range(0, 180)]
    public float spawnStart;  // Απο τι μοίρες να ξεκινήσει να spawnarei
    public float frontBackVariance; 
    public float leftRightVariance;
    public float charSpace;    // Space between characters in deg



    // Define general spawn position (line behind main characters)
    private float spawnY;   
    

    public int n_chars = 20;
    private float tmp_frontBackOffset; 
    private float tmp_leftRightOffset;
 
 
    // Start is called before the first frame update
    void Start() { 
        spawnY = centerPoint.transform.position.y - 1.1f;           // Σε τι ύψος
                
        spawnCirc(1.8f);
        spawnCirc(2.4f);
        spawnCirc(3f);

        // spawnLine(4);
        // spawnLine(6);

    }

    // Update is called once per frame
    void Update() {
        
    }

    void spawnCirc(float radius){
        for (int i = 0; i < n_chars; i++) {

            // Get the randoms
            tmp_frontBackOffset = Random.Range(-frontBackVariance, frontBackVariance);
            tmp_leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);

            // Calculate spawn position
            float spawnX = - (float) ( radius * Mathf.Cos(Mathf.Deg2Rad * (spawnStart + i*charSpace )) + tmp_leftRightOffset);
            float spawnZ = (float) ( radius * Mathf.Sin(Mathf.Deg2Rad * (spawnStart + i*charSpace )) + tmp_frontBackOffset);
            Vector3 spawnPos = new Vector3(spawnX, spawnY, spawnZ);

            // Select random model to spawn
            int randomModel =  Random.Range(0, charPrefab_array.Length);

            // Spawn the character
            GameObject clone = Instantiate(charPrefab_array[randomModel], spawnPos, Quaternion.identity, transform);

            // Get the angle between current character and center point
            var rot = Mathf.Atan2(spawnX - centerPoint.transform.position.x, spawnZ-centerPoint.transform.position.z) * Mathf.Rad2Deg;

            // Rotate the character
            clone.transform.Rotate(0f, rot+180, 0f);

            // Decide if the character will be animated or not
            int t = Random.Range(0,2);
            if (t == 1){
                clone.GetComponent<bgChar_script>().activeAnim = 1;

                int team = Random.Range(0,2);
                if (team == 1){
                    clone.GetComponent<bgChar_script>().teamLeft = true;
                }else{
                    clone.GetComponent<bgChar_script>().teamRight = true;
                }
            }
        }
    }
}
