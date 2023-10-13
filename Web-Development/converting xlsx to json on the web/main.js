const file_uploader = document.getElementById("file_uploader");

const parseUploadedFile = async (file) => {
  const onFileReaderLoad = function (e, resolve) {
    const bufferArray = e.target.result;

    const wb = XLSX.read(bufferArray, { type: "buffer" });

    const wsname = wb.SheetNames[0];

    const ws = wb.Sheets[wsname];

    const data = XLSX.utils.sheet_to_json(ws);

    resolve(data);
  };

  const readExcel = (file) => {
    const promise = new Promise((resolve, reject) => {
      const fileReader = new FileReader();
      fileReader.readAsArrayBuffer(file);
      fileReader.onload = (e) => onFileReaderLoad(e, resolve);
      fileReader.onerror = (error) => reject(error);
    });

    return promise;
  };

  if (!file) return undefined;

  const ext = file.name.split(".")?.pop();

  if (ext === "xlsx") {
    return await readExcel(file);
  } else {
    alert("File must be a valid .xlsx file");
    return;
  }
};

const parser = async (e) => {
  try {
    console.log("parsing....");
    const file = e.target.files[0];

    const result = await parseUploadedFile(file);

    if (typeof result === "object" && Array.isArray(result)) {
      const thead_row = document.getElementById("th_tr"),
        tbody = document.getElementById("tbody");

      const heading = result[0];

      if (typeof heading !== "object") {
        throw new Error("The .xlsx list MUST be a valid list of objects");
      }

      const keys = Object.keys(heading);

      keys.forEach((key) => {
        thead_row.innerHTML += `<td>${key?.toUpperCase()}</td>`;
      });

      result.forEach((obj) => {
        const values = Object.values(obj);

        tbody.innerHTML += `<tr>
                ${values.map((value) => `<td>${value}</td>`)}
            </tr>`;
      });
    } else {
      throw new Error("The .xlsx file contents MUST be a valid list");
    }
  } catch (err) {
    console.log("ERR: ", err);
    alert("An error occurred");
  }
};

file_uploader.addEventListener("change", parser);
