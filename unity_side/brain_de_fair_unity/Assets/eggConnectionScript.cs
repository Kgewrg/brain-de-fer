
using System.Diagnostics;
using Unity.VisualScripting;
using UnityEngine;


public class eggConnectionScript : MonoBehaviour
{

    // TODO: Να μπορείς να διαλέξεις recoderd (μέσο player prefs)
    private string pythonPath = "C:\\Users\\tsarosDesktop\\AppData\\Local\\Microsoft\\WindowsApps\\python3.10.exe";
    private string scriptPath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\recorderOriginal.py";
    Process pyProcess = new Process();

    static eggConnectionScript instance;    

    void Awake() {
        
        // Για να μην διαγράφεται στο reload
        if (instance != null){
            Destroy(gameObject);
        }
        else{
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        

        ProcessStartInfo startInfo = new ProcessStartInfo();
        startInfo.FileName = pythonPath;
        startInfo.Arguments = scriptPath;
        startInfo.UseShellExecute = false;
        startInfo.RedirectStandardOutput = true;
        startInfo.CreateNoWindow = true;

        pyProcess.StartInfo = startInfo;
        pyProcess.Start();
    }



    void OnDestroy(){
        // Κλείνει το python όταν σταματάει το παιχνίδι 
        if (pyProcess != null && !pyProcess.HasExited) {
            pyProcess.Kill();
            pyProcess.Close();
            pyProcess.Dispose();
        }
    }
}
