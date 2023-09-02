
using System.Diagnostics;
using Unity.VisualScripting;
using UnityEngine;


public class eggConnectionScript : MonoBehaviour
{
    // Start is called before the first frame update
    private string pythonPath = "C:\\Users\\tsarosDesktop\\AppData\\Local\\Microsoft\\WindowsApps\\python3.10.exe";
    private string scriptPath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\recorderOriginal.py";
    Process pyProcess = new Process();

    static eggConnectionScript instance;    

    void Awake() {

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
        if (pyProcess != null && !pyProcess.HasExited) {
            pyProcess.Kill();
            pyProcess.Close();
            pyProcess.Dispose();
        }
    }
}
