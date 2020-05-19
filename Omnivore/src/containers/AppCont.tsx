import { Provider, Subscribe, Container } from 'unstated-typescript';

type AppState = {
    count: number
  };

class AppCont extends Container<AppState> {
    state = { 
        count: 0 
    };

}

export default AppCont;