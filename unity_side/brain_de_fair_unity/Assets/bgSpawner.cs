using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{

    public GameObject[] charPrefab_array;
    public GameObject centerPoint; 
    public float frontBackVariance; 
    public float leftRightVariance;
 
    // Start is called before the first frame update
    void Start() {
        

        
        // Define general spawn position (line behind main characters)
        float spawnZ_line = centerPoint.transform.position.z + 60;
        float spawnLeftOffset = centerPoint.transform.position.x - 130;
        float spawnRightOffset = centerPoint.transform.position.x + 100;
        float spawnY = centerPoint.transform.position.y - 49;
        float charSpace = 25;    // Space between characters
        

        int n_chars = 12;
        float tmp_frontBackOffset; 
        float tmp_leftRightOffset;

  
        // First line (bot to top)
        for (int i = 0; i < n_chars; i++) {
            // Debug.Log("spawing line 1");

            // Get the randoms
            tmp_frontBackOffset = Random.Range(-frontBackVariance, frontBackVariance);
            tmp_leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);

            // Figure out spawn positions
            float spawnX = (float)(spawnLeftOffset + (i*charSpace));
            float spawnZ = spawnZ_line + tmp_frontBackOffset - 10; // -10 για να είναι η πιο κοντά γραμμή
            Vector3 spawnPos = new Vector3(spawnX, spawnY, spawnZ);

            // Select random model to spawn
            int randomModel =  Random.Range(0, charPrefab_array.Length);

            // Spawn the character
            GameObject clone = Instantiate(charPrefab_array[randomModel], spawnPos, Quaternion.identity, centerPoint.transform);

            // Get the angle between current character and center point
            var rot = Mathf.Atan2(spawnX - centerPoint.transform.position.x, spawnZ-centerPoint.transform.position.z) * Mathf.Rad2Deg;

            // Rotate the character
            clone.transform.Rotate(0f, rot+180, 0f);

            // Decide if the character will be animated or not
            int t = Random.Range(0,2);
            if (t == 1){
               clone.GetComponent<bgChar_script>().activeAnim = 1;
            }
        }

        
        for (int i = 0; i < n_chars; i++) {
            // Debug.Log("spawing line 2");

            // Get the randoms
            tmp_frontBackOffset = Random.Range(-frontBackVariance, frontBackVariance);
            tmp_leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);

            // Figure out spawn positions
            float spawnX = (float)(spawnLeftOffset + (i*charSpace));
            float spawnZ = spawnZ_line + tmp_frontBackOffset;           // μεσέα γραμμή
            Vector3 spawnPos = new Vector3(spawnX, spawnY, spawnZ);

            // Select random model to spawn
            int randomModel =  Random.Range(0, charPrefab_array.Length);

            // Spawn the character
            GameObject clone = Instantiate(charPrefab_array[randomModel], spawnPos, Quaternion.identity, centerPoint.transform);

            // Get the angle between current character and center point
            var rot = Mathf.Atan2(spawnX - centerPoint.transform.position.x, spawnZ-centerPoint.transform.position.z) * Mathf.Rad2Deg;

            // Rotate the character
            clone.transform.Rotate(0f, rot+180, 0f);

            // Decide if the character will be animated or not
            int t = Random.Range(0,2);
            if (t == 1){
               clone.GetComponent<bgChar_script>().activeAnim = 1;
            }
        }

        for (int i = 0; i < n_chars; i++) {
            // Debug.Log("spawing line 3");

            // Get the randoms
            tmp_frontBackOffset = Random.Range(-frontBackVariance, frontBackVariance);
            tmp_leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);

            // Figure out spawn positions
            float spawnX = (float)(spawnLeftOffset + (i*charSpace));
            float spawnZ = spawnZ_line + tmp_frontBackOffset + 10; // +10 για να είναι η πιο μακριά γραμμή
            Vector3 spawnPos = new Vector3(spawnX, spawnY, spawnZ);

            // Select random model to spawn
            int randomModel =  Random.Range(0, charPrefab_array.Length);

            // Spawn the character
            GameObject clone = Instantiate(charPrefab_array[randomModel], spawnPos, Quaternion.identity, centerPoint.transform);

            // Get the angle between current character and center point
            var rot = Mathf.Atan2(spawnX - centerPoint.transform.position.x, spawnZ-centerPoint.transform.position.z) * Mathf.Rad2Deg;

            // Rotate the character
            clone.transform.Rotate(0f, rot+180, 0f);

            // Decide if the character will be animated or not
            int t = Random.Range(0,2);
            if (t == 1){
               clone.GetComponent<bgChar_script>().activeAnim = 1;
            }
        }


        // for (int i = 0; i < n_chars+1; i++) {
        //     // Debug.Log("spawing line 4");
        //     frontBackOffset = Random.Range(-variance, variance);
        //     leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);
        //     GameObject clone = Instantiate(charPrefab, new Vector3((float)(spawnLeftOffset + (i*sideDist)), spawnY, spawnZ+frontBackOffset), Quaternion.identity);
        //     int t = Random.Range(0,2);
        //     if (t == 1){
        //        clone.GetComponent<bgChar_script>().activeAnim = 1;
        //     }
        // }
        
    }

    // Update is called once per frame
    void Update() {
        
    }
}
